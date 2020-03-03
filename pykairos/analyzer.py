#    This file is part of Kairos.
#
#    Kairos is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Kairos is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Kairos.  If not, see <http://www.gnu.org/licenses/>.
#

import os, logging, re, sys, lxml.html, json

class Object: pass

class Analyzer:
    def __init__(s, c, scope, emitlistener, listenercontext):
        s.configurator = c
        s.rules = []
        s.contextrules = {}
        s.common = {}
        s.outcontextrules = []
        s.context = ''
        s.actions = {}
        s.gcpt = 0;
        s.listener = emitlistener
        s.listenercontext = listenercontext
        s.scope = scope
        s.name = c['id']
        try: s.behaviour = os.environ['ANALYZER_BEHAVIOUR']
        except: s.behaviour = 'OLD'
        logging.trace("Analyzer behaviour: " + s.behaviour)
        logging.trace(s.name + ' - Init Analyzer()')
        if "rules" in c:
            for r in c["rules"]:
                if  not "scope" in r or r["scope"] in scope or '*' in scope: s.addRule(r)
        if "contextrules" in c:
            for r in c["contextrules"]:
                if  not "scope" in r or r["scope"] in scope or '*' in scope: s.addContextRule(r)
        if "outcontextrules" in c:
            for r in c["outcontextrules"]:
                if  not "scope" in r or r["scope"] in scope or '*' in scope: s.addOutContextRule(r)
        if "begin" in c: s.addContextRule({"context": "BEGIN", "action": c["begin"], "regexp": '.'})
        if "end" in c: s.addContextRule({"context": "END", "action": c["end"], "regexp": '.'})
    def trace(s, m):
        logging.trace(s.name + ' - ' + m)
    def addRule(s, r):
        logging.trace(s.name + ' - Adding rule, regular expression: /' + r["regexp"] + '/, action: ' + r["action"].__name__)
        if 'tag' in r: s.rules.append({"action": r["action"], "regexp": re.compile(r["regexp"]), "tag": re.compile(r["tag"])})
        else: s.rules.append({"action": r["action"], "regexp": re.compile(r["regexp"])})
    def addOutContextRule(s, r):
        logging.trace(s.name + ' - Adding out context rule, regular expression: /' + r["regexp"] + '/, action: ' + r["action"].__name__)
        if 'tag' in r: s.outcontextrules.append({"action": r["action"], "regexp": re.compile(r["regexp"]), "tag": re.compile(r["tag"])})
        else: s.outcontextrules.append({"action": r["action"], "regexp": re.compile(r["regexp"])})
    def addContextRule(s, r):
        logging.trace(s.name + ' - Adding context rule, context: ' + r["context"] + ', regular expression: /' + r["regexp"] + '/, action: ' + r["action"].__name__)
        if 'tag' in r: s.contextrules[r["context"]] = {"action": r["action"], "regexp": re.compile(r["regexp"]), "tag": re.compile(r["tag"])}
        else: s.contextrules[r["context"]] = {"action": r["action"], "regexp": re.compile(r["regexp"])}
    def setContext(s, c):
        logging.trace(s.name + ' - Setting context: ' + c)
        s.context = c
    def emit(s, col, d, v):
        s.stats["rec"] += 1
        s.listener(col, d, v, s.listenercontext)
        s.gcpt += 1
        logging.trace(json.dumps(d))
    def analyze(s, stream, name):
        logging.trace(s.name + ' - Scope: ' + str(s.scope))
        if "content" in s.configurator and s.configurator["content"] == "xml": return s.analyzexml(stream.decode(), name)
        elif "content" in s.configurator and s.configurator["content"] == "json": return s.analyzejson(stream.decode(), name)
        else: return s.analyzestr(stream.decode(errors="ignore"), name)
    def analyzestr(s, stream, name):
        status = Object()
        status.error = None
        logging.trace(s.name + ' - Analyzing stream ' + name)
        s.context = ''
        s.stats = dict(lines=0, ger=0, sger=0, cer=0, scer=0, oer=0, soer=0, rec=0)
        try:
            if "BEGIN" in s.contextrules:
                logging.trace(s.name + ' - Calling BEGIN at line ' + str(s.stats["lines"]))
                s.contextrules["BEGIN"]["action"](s)
            for ln in stream.split('\n'):
                ln=ln.rstrip('\r')
                if s.context == 'BREAK': break
                s.stats['lines'] += 1
                for r in s.rules:
                    s.stats['ger'] += 1
                    p = r["regexp"].search(ln)
                    if not p: continue
                    s.stats['sger'] += 1
                    logging.trace(s.name + ' - Calling ' + r["action"].__name__ + ' at line ' + str(s.stats["lines"]) + ' containing: |' + ln + '|')
                    r["action"](s, ln, p.group, name)
                if s.context == '':
                    outr = s.outcontextrules[0:1] if s.behaviour == 'NEW' else s.outcontextrules
                    for r in outr:           
                        s.stats['oer'] += 1
                        p = r["regexp"].search(ln)
                        if not p: continue
                        s.outcontextrules = s.outcontextrules[1:] if s.behaviour == 'NEW' else s.outcontextrules                 
                        s.stats['soer'] += 1
                        logging.trace(s.name + ' - Calling ' + r["action"].__name__ + ' at line ' + str(s.stats["lines"]) + ' containing: |' + ln + '|')
                        r["action"](s, ln, p.group, name)
                        break
                if s.context in s.contextrules:
                    r = s.contextrules[s.context]
                    s.stats['cer'] += 1
                    p = r["regexp"].search(ln)
                    if not p: continue
                    s.stats['scer'] += 1
                    logging.trace(s.name + ' - Calling ' + r["action"].__name__ + ' at line ' + str(s.stats["lines"]) + ' containing: |' + ln + '|')
                    r["action"](s, ln, p.group, name)
            if "END" in s.contextrules:
                logging.trace(s.name + ' - Calling END at line ' + str(s.stats["lines"]))
                s.contextrules["END"]["action"](s)
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(s.name + ' - ' + name + ' - ' + message)
            logging.error(s.name + ' at line: ' + ln)
            status.error = message
        logging.info(s.name + ' - Summary for member ' + name);
        logging.info(s.name + ' -    Analyzed lines              : ' + str(s.stats["lines"]))
        logging.info(s.name + ' -    Evaluated rules (global)    : ' + str(s.stats["ger"]))
        logging.info(s.name + ' -    Satisfied rules (global)    : ' + str(s.stats["sger"]))
        logging.info(s.name + ' -    Evaluated rules (outcontext): ' + str(s.stats["oer"]))
        logging.info(s.name + ' -    Satisfied rules (outcontext): ' + str(s.stats["soer"]))
        logging.info(s.name + ' -    Evaluated rules (context)   : ' + str(s.stats["cer"]))
        logging.info(s.name + ' -    Satisfied rules (context)   : ' + str(s.stats["scer"]))
        logging.info(s.name + ' -    Emitted records             : ' + str(s.stats["rec"]))
        return status
    def analyzejson(s, stream, name):
        status = Object()
        status.error = None        
        logging.trace(s.name + ' - Analyzing stream' + name)
        s.stats = dict(lines=0, er=0, ser=0, rec=0)
        d = json.loads(stream)
        for x in d['data']: s.emit(d['collection'], d['desc'], x)
        logging.info(s.name + ' - Summary for member ' + name);
        logging.info(s.name + ' -    Emitted records  : ' + str(s.stats["rec"]))
        return status
    def lxmltext1(s, e):
        r = e.text.replace('\n','').replace('\r','').lstrip().rstrip() if type(e.text) == type('') else ''
        if not r and e.tag in  ['td', 'h3']:
            for x in e.itertext():
                if x != '':
                    r = x
                    break
        return r
    def lxmltext2(s, e):
        return e.text_content().replace('\n','').replace('\r','').lstrip().rstrip()
    def analyzexml(s, stream, name):
        status = Object()
        status.error = None        
        logging.trace(s.name + ' - Analyzing xml stream' + name)
        s.context = ''
        s.stats = dict(patterns=0, ger=0, sger=0, cer=0, scer=0, oer=0, soer=0, rec=0)
        try:
            page=fromstring(stream)
            s.lxmltext = s.lxmltext1
        except:
            page=lxml.html.fromstring(stream)
            s.lxmltext = s.lxmltext2
        if "BEGIN" in s.contextrules:
            logging.trace(s.name + ' - Calling BEGIN at pattern ' + str(s.stats["patterns"]))
            s.contextrules["BEGIN"]["action"](s)
        for ln in page.getiterator():
            if s.context == 'BREAK': break
            s.stats['patterns'] += 1
            for r in s.rules:
                s.stats['ger'] += 1
                p = r["tag"].search(ln.tag)
                if not p: continue
                p = r["regexp"].search(s.lxmltext(ln))
                if not p: continue
                s.stats['sger'] += 1
                logging.trace(s.name + ' - Calling ' + r["action"].__name__ + ' at text ' + s.lxmltext(ln) + ' for tag: ' + ln.tag)
                r["action"](s, ln, p.group, name)
                if s.context == 'BREAK': break
            if s.context == '':
                outr = s.outcontextrules[0:1] if s.behaviour == 'NEW' else s.outcontextrules
                for r in outr:           
                    s.stats['oer'] += 1
                    p = r["tag"].search(ln.tag)
                    if not p: continue
                    p = r["regexp"].search(s.lxmltext(ln))
                    if not p: continue
                    s.outcontextrules = s.outcontextrules[1:] if s.behaviour == 'NEW' else s.outcontextrules                 
                    s.stats['soer'] += 1
                    logging.trace(s.name + ' - Calling ' + r["action"].__name__ + ' at text ' + s.lxmltext(ln) + ' for tag: ' + ln.tag)
                    r["action"](s, ln, p.group, name)
                    break
            if s.context in s.contextrules:
                r = s.contextrules[s.context]
                s.stats['cer'] += 1
                p = r["tag"].search(ln.tag)
                if not p: continue
                p = r["regexp"].search(s.lxmltext(ln))
                if not p: continue
                s.stats['scer'] += 1
                logging.trace(s.name + ' - Calling ' + r["action"].__name__ + ' at text ' + s.lxmltext(ln) + ' for tag: ' + ln.tag)
                r["action"](s, ln, p.group, name)
        if "END" in s.contextrules:
            logging.trace(s.name + ' - Calling END at pattern ' + str(s.stats["patterns"]))
            s.contextrules["END"]["action"](s)
        logging.info(s.name + ' - Summary for member ' + name);
        logging.info(s.name + ' -    Analyzed patterns   : ' + str(s.stats["patterns"]))
        logging.info(s.name + ' -    Evaluated rules (global)    : ' + str(s.stats["ger"]))
        logging.info(s.name + ' -    Satisfied rules (global)    : ' + str(s.stats["sger"]))
        logging.info(s.name + ' -    Evaluated rules (outcontext): ' + str(s.stats["oer"]))
        logging.info(s.name + ' -    Satisfied rules (outcontext): ' + str(s.stats["soer"]))
        logging.info(s.name + ' -    Evaluated rules (context)   : ' + str(s.stats["cer"]))
        logging.info(s.name + ' -    Satisfied rules (context)   : ' + str(s.stats["scer"]))
        logging.info(s.name + ' -    Emitted records             : ' + str(s.stats["rec"]))
        return status
