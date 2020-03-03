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

logging.TRACE = 5
logging.addLevelName(5, "TRACE")
logging.trace = lambda m: logging.log(logging.TRACE, m)

class Object: pass

class Analyzer:
    def __init__(self, c, scope, emitlistener, listenercontext):
        self.configurator = c
        self.rules = []
        self.contextrules = {}
        self.common = {}
        self.outcontextrules = []
        self.context = ''
        self.actions = {}
        self.gcpt = 0
        self.listener = emitlistener
        self.listenercontext = listenercontext
        self.scope = scope
        self.name = c['id']
        try: self.behaviour = os.environ['ANALYZER_BEHAVIOUR']
        except: self.behaviour = 'OLD'
        logging.trace("Analyzer behaviour: " + self.behaviour)
        logging.trace(self.name + ' - Init Analyzer()')
        if "rules" in c:
            for r in c["rules"]:
                if  not "scope" in r or r["scope"] in scope or '*' in scope: self.addRule(r)
        if "contextrules" in c:
            for r in c["contextrules"]:
                if  not "scope" in r or r["scope"] in scope or '*' in scope: self.addContextRule(r)
        if "outcontextrules" in c:
            for r in c["outcontextrules"]:
                if  not "scope" in r or r["scope"] in scope or '*' in scope: self.addOutContextRule(r)
        if "begin" in c: self.addContextRule({"context": "BEGIN", "action": c["begin"], "regexp": '.'})
        if "end" in c: self.addContextRule({"context": "END", "action": c["end"], "regexp": '.'})
    def trace(self, m):
        logging.trace(self.name + ' - ' + m)
    def addRule(self, r):
        logging.trace(self.name + ' - Adding rule, regular expression: /' + r["regexp"] + '/, action: ' + r["action"].__name__)
        if 'tag' in r: self.rules.append({"action": r["action"], "regexp": re.compile(r["regexp"]), "tag": re.compile(r["tag"])})
        else: self.rules.append({"action": r["action"], "regexp": re.compile(r["regexp"])})
    def addOutContextRule(self, r):
        logging.trace(self.name + ' - Adding out context rule, regular expression: /' + r["regexp"] + '/, action: ' + r["action"].__name__)
        if 'tag' in r: self.outcontextrules.append({"action": r["action"], "regexp": re.compile(r["regexp"]), "tag": re.compile(r["tag"])})
        else: self.outcontextrules.append({"action": r["action"], "regexp": re.compile(r["regexp"])})
    def addContextRule(self, r):
        logging.trace(self.name + ' - Adding context rule, context: ' + r["context"] + ', regular expression: /' + r["regexp"] + '/, action: ' + r["action"].__name__)
        if 'tag' in r: self.contextrules[r["context"]] = {"action": r["action"], "regexp": re.compile(r["regexp"]), "tag": re.compile(r["tag"])}
        else: self.contextrules[r["context"]] = {"action": r["action"], "regexp": re.compile(r["regexp"])}
    def setContext(self, c):
        logging.trace(self.name + ' - Setting context: ' + c)
        self.context = c
    def emit(self, col, d, v):
        self.stats["rec"] += 1
        self.listener(col, d, v, self.listenercontext)
        self.gcpt += 1
        logging.trace(json.dumps(d))
    def analyze(self, stream, name):
        logging.trace(self.name + ' - Scope: ' + str(self.scope))
        if "content" in self.configurator and self.configurator["content"] == "xml": return self.analyzexml(stream.decode(), name)
        elif "content" in self.configurator and self.configurator["content"] == "json": return self.analyzejson(stream.decode(), name)
        else: return self.analyzestr(stream.decode(errors="ignore"), name)
    def analyzestr(self, stream, name):
        status = Object()
        status.error = None
        logging.trace(self.name + ' - Analyzing stream ' + name)
        self.context = ''
        self.stats = dict(lines=0, ger=0, sger=0, cer=0, scer=0, oer=0, soer=0, rec=0)
        try:
            if "BEGIN" in self.contextrules:
                logging.trace(self.name + ' - Calling BEGIN at line ' + str(self.stats["lines"]))
                self.contextrules["BEGIN"]["action"](self)
            for ln in stream.split('\n'):
                ln=ln.rstrip('\r')
                if self.context == 'BREAK': break
                self.stats['lines'] += 1
                for r in self.rules:
                    self.stats['ger'] += 1
                    p = r["regexp"].search(ln)
                    if not p: continue
                    self.stats['sger'] += 1
                    logging.trace(self.name + ' - Calling ' + r["action"].__name__ + ' at line ' + str(self.stats["lines"]) + ' containing: |' + ln + '|')
                    r["action"](self, ln, p.group, name)
                if self.context == '':
                    outr = self.outcontextrules[0:1] if self.behaviour == 'NEW' else self.outcontextrules
                    for r in outr:           
                        self.stats['oer'] += 1
                        p = r["regexp"].search(ln)
                        if not p: continue
                        self.outcontextrules = self.outcontextrules[1:] if self.behaviour == 'NEW' else self.outcontextrules                 
                        self.stats['soer'] += 1
                        logging.trace(self.name + ' - Calling ' + r["action"].__name__ + ' at line ' + str(self.stats["lines"]) + ' containing: |' + ln + '|')
                        r["action"](self, ln, p.group, name)
                        break
                if self.context in self.contextrules:
                    r = self.contextrules[self.context]
                    self.stats['cer'] += 1
                    p = r["regexp"].search(ln)
                    if not p: continue
                    self.stats['scer'] += 1
                    logging.trace(self.name + ' - Calling ' + r["action"].__name__ + ' at line ' + str(self.stats["lines"]) + ' containing: |' + ln + '|')
                    r["action"](self, ln, p.group, name)
            if "END" in self.contextrules:
                logging.trace(self.name + ' - Calling END at line ' + str(self.stats["lines"]))
                self.contextrules["END"]["action"](self)
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(self.name + ' - ' + name + ' - ' + message)
            logging.error(self.name + ' at line: ' + ln)
            status.error = message
        logging.info(self.name + ' - Summary for member ' + name)
        logging.info(self.name + ' -    Analyzed lines              : ' + str(self.stats["lines"]))
        logging.info(self.name + ' -    Evaluated rules (global)    : ' + str(self.stats["ger"]))
        logging.info(self.name + ' -    Satisfied rules (global)    : ' + str(self.stats["sger"]))
        logging.info(self.name + ' -    Evaluated rules (outcontext): ' + str(self.stats["oer"]))
        logging.info(self.name + ' -    Satisfied rules (outcontext): ' + str(self.stats["soer"]))
        logging.info(self.name + ' -    Evaluated rules (context)   : ' + str(self.stats["cer"]))
        logging.info(self.name + ' -    Satisfied rules (context)   : ' + str(self.stats["scer"]))
        logging.info(self.name + ' -    Emitted records             : ' + str(self.stats["rec"]))
        return status
    def analyzejson(self, stream, name):
        status = Object()
        status.error = None        
        logging.trace(self.name + ' - Analyzing stream' + name)
        self.stats = dict(lines=0, er=0, ser=0, rec=0)
        d = json.loads(stream)
        for x in d['data']: self.emit(d['collection'], d['desc'], x)
        logging.info(self.name + ' - Summary for member ' + name)
        logging.info(self.name + ' -    Emitted records  : ' + str(self.stats["rec"]))
        return status
    def lxmltext1(self, e):
        r = e.text.replace('\n','').replace('\r','').lstrip().rstrip() if type(e.text) == type('') else ''
        if not r and e.tag in  ['td', 'h3']:
            for x in e.itertext():
                if x != '':
                    r = x
                    break
        return r
    def lxmltext2(self, e):
        return e.text_content().replace('\n','').replace('\r','').lstrip().rstrip()
    def analyzexml(self, stream, name):
        status = Object()
        status.error = None        
        logging.trace(self.name + ' - Analyzing xml stream' + name)
        self.context = ''
        self.stats = dict(patterns=0, ger=0, sger=0, cer=0, scer=0, oer=0, soer=0, rec=0)
        try:
            page=fromstring(stream)
            self.lxmltext = self.lxmltext1
        except:
            page=lxml.html.fromstring(stream)
            self.lxmltext = self.lxmltext2
        if "BEGIN" in self.contextrules:
            logging.trace(self.name + ' - Calling BEGIN at pattern ' + str(self.stats["patterns"]))
            self.contextrules["BEGIN"]["action"](self)
        for ln in page.getiterator():
            if self.context == 'BREAK': break
            self.stats['patterns'] += 1
            for r in self.rules:
                self.stats['ger'] += 1
                p = r["tag"].search(ln.tag)
                if not p: continue
                p = r["regexp"].search(self.lxmltext(ln))
                if not p: continue
                self.stats['sger'] += 1
                logging.trace(self.name + ' - Calling ' + r["action"].__name__ + ' at text ' + self.lxmltext(ln) + ' for tag: ' + ln.tag)
                r["action"](self, ln, p.group, name)
                if self.context == 'BREAK': break
            if self.context == '':
                outr = self.outcontextrules[0:1] if self.behaviour == 'NEW' else self.outcontextrules
                for r in outr:           
                    self.stats['oer'] += 1
                    p = r["tag"].search(ln.tag)
                    if not p: continue
                    p = r["regexp"].search(self.lxmltext(ln))
                    if not p: continue
                    self.outcontextrules = self.outcontextrules[1:] if self.behaviour == 'NEW' else self.outcontextrules                 
                    self.stats['soer'] += 1
                    logging.trace(self.name + ' - Calling ' + r["action"].__name__ + ' at text ' + self.lxmltext(ln) + ' for tag: ' + ln.tag)
                    r["action"](self, ln, p.group, name)
                    break
            if self.context in self.contextrules:
                r = self.contextrules[self.context]
                self.stats['cer'] += 1
                p = r["tag"].search(ln.tag)
                if not p: continue
                p = r["regexp"].search(self.lxmltext(ln))
                if not p: continue
                self.stats['scer'] += 1
                logging.trace(self.name + ' - Calling ' + r["action"].__name__ + ' at text ' + self.lxmltext(ln) + ' for tag: ' + ln.tag)
                r["action"](self, ln, p.group, name)
        if "END" in self.contextrules:
            logging.trace(self.name + ' - Calling END at pattern ' + str(self.stats["patterns"]))
            self.contextrules["END"]["action"](self)
        logging.info(self.name + ' - Summary for member ' + name)
        logging.info(self.name + ' -    Analyzed patterns   : ' + str(self.stats["patterns"]))
        logging.info(self.name + ' -    Evaluated rules (global)    : ' + str(self.stats["ger"]))
        logging.info(self.name + ' -    Satisfied rules (global)    : ' + str(self.stats["sger"]))
        logging.info(self.name + ' -    Evaluated rules (outcontext): ' + str(self.stats["oer"]))
        logging.info(self.name + ' -    Satisfied rules (outcontext): ' + str(self.stats["soer"]))
        logging.info(self.name + ' -    Evaluated rules (context)   : ' + str(self.stats["cer"]))
        logging.info(self.name + ' -    Satisfied rules (context)   : ' + str(self.stats["scer"]))
        logging.info(self.name + ' -    Emitted records             : ' + str(self.stats["rec"]))
        return status
