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
from collections import Counter, OrderedDict

logging.TRACE = 5
logging.addLevelName(5, "TRACE")
logging.trace = lambda m: logging.log(logging.TRACE, m)

def xxxx(e):
    #return e.text_content().replace('\n','').replace('\r','').lstrip().rstrip()
    return e.text_content().strip(' \n\r')

class Object: pass

class Analyzer:
    def __init__(self, c, scope, emitlistener, listenercontext):
        self.configurator = c
        self.rules = OrderedDict()
        self.contextrules = OrderedDict()
        self.common = {}
        self.outcontextrules = OrderedDict()
        self.context = ''
        self.actions = {}
        self.gcpt = 0
        self.listener = emitlistener
        self.listenercontext = listenercontext
        self.scope = scope
        self.name = c['id']
        logging.trace(f'{self.name} - Init Analyzer()')
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
        logging.trace(f'{self.name} - {m}')
    def addRule(self, r):
        if 'tag' not in r: r["tag"] = 'missing'
        logging.trace(f'{self.name} - Adding rule, tag: {r["tag"]}, regular expression: /{r["regexp"]}/, action: {r["action"].__name__}')
        d = dict(action=r["action"], regexp=re.compile(r["regexp"]), tag=re.compile(r["tag"]))
        if d['tag'] not in self.rules: self.rules[d['tag']] = []
        self.rules[d['tag']].append(d)
    def addOutContextRule(self, r):
        if 'tag' not in r: r["tag"] = 'missing'
        logging.trace(f'{self.name} - Adding outcontext rule, tag: {r["tag"]}, regular expression: /{r["regexp"]}/, action: {r["action"].__name__}')
        d = dict(action=r["action"], regexp=re.compile(r["regexp"]), tag=re.compile(r["tag"]))
        if d['tag'] not in self.outcontextrules: self.outcontextrules[d['tag']] = []
        self.outcontextrules[d['tag']].append(d)
    def addContextRule(self, r):
        if 'tag' not in r: r["tag"] = 'missing'
        logging.trace(f'{self.name} - Adding context rule, tag: {r["tag"]}, context: {r["context"]}, regular expression: /{r["regexp"]}/, action: {r["action"].__name__}')
        self.contextrules[r["context"]] = dict(action=r["action"], regexp=re.compile(r["regexp"]), tag=re.compile(r["tag"]))
    def setContext(self, c):
        logging.trace(f'{self.name} - Setting context: {c}')
        self.context = c
    def emit(self, col, d, v):
        self.stats["rec"] += 1
        self.listener(col, d, v, self.listenercontext)
        self.gcpt += 1
        logging.trace(json.dumps(d))
    def analyze(self, stream, name):
        logging.trace(f'{self.name} - Scope: {self.scope}')
        if "content" in self.configurator and self.configurator["content"] == "xml": return self.analyzexml(stream.decode(), name)
        elif "content" in self.configurator and self.configurator["content"] == "json": return self.analyzejson(stream.decode(), name)
        else: return self.analyzestr(stream.decode(errors="ignore"), name)
    def analyzestr(self, stream, name):
        status = Object()
        status.error = None
        logging.trace(f'{self.name} - Analyzing stream {name}')
        self.context = ''
        self.stats = Counter()
        try:
            if "BEGIN" in self.contextrules:
                logging.trace(f'{self.name} - Calling BEGIN at line {self.stats["lines"]}')
                self.contextrules["BEGIN"]["action"](self)
            for ln in stream.split('\n'):
                ln=ln.rstrip('\r')
                if self.context == 'BREAK': break
                self.stats['lines'] += 1
                for t in self.rules:
                    for r in self.rules[t]:
                        self.stats['ger'] += 1
                        p = r["regexp"].search(ln)
                        if not p: continue
                        self.stats['sger'] += 1
                        logging.trace(f'{self.name} - Calling {r["action"].__name__} at line {self.stats["lines"]} containing: |{ln}|')
                        r["action"](self, ln, p.group, name)
                        if self.context == 'BREAK': break
                if self.context == '':
                    for t in self.outcontextrules:
                        for r in self.outcontextrules[t]:           
                            self.stats['oer'] += 1
                            p = r["regexp"].search(ln)
                            if not p: continue
                            self.stats['soer'] += 1
                            logging.trace(f'{self.name} - Calling {r["action"].__name__} at line {self.stats["lines"]} containing: |{ln}|')
                            r["action"](self, ln, p.group, name)
                            break
                if self.context in self.contextrules:
                    r = self.contextrules[self.context]
                    self.stats['cer'] += 1
                    p = r["regexp"].search(ln)
                    if not p: continue
                    self.stats['scer'] += 1
                    logging.trace(f'{self.name} - Calling {r["action"].__name__} at line {self.stats["lines"]} containing: |{ln}|')
                    r["action"](self, ln, p.group, name)
            if "END" in self.contextrules:
                logging.trace(f'{self.name} - Calling END at line {self.stats["lines"]}')
                self.contextrules["END"]["action"](self)
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(f'{self.name} - {name} - {message}')
            logging.error(f'{self.name} at line: {ln}')
            status.error = message
        logging.info(f'{self.name} - Summary for member {name}')
        logging.info(f'{self.name} -    Analyzed lines              : {self.stats["lines"]}')
        logging.info(f'{self.name} -    Evaluated rules (global)    : {self.stats["ger"]}')
        logging.info(f'{self.name} -    Satisfied rules (global)    : {self.stats["sger"]}')
        logging.info(f'{self.name} -    Evaluated rules (outcontext): {self.stats["oer"]}')
        logging.info(f'{self.name} -    Satisfied rules (outcontext): {self.stats["soer"]}')
        logging.info(f'{self.name} -    Evaluated rules (context)   : {self.stats["cer"]}')
        logging.info(f'{self.name} -    Satisfied rules (context)   : {self.stats["scer"]}')
        logging.info(f'{self.name} -    Emitted records             : {self.stats["rec"]}')
        return status
    def analyzejson(self, stream, name):
        status = Object()
        status.error = None        
        logging.trace(f'{self.name} - Analyzing stream {name}')
        self.stats = Counter()
        d = json.loads(stream)
        for x in d['data']: self.emit(d['collection'], d['desc'], x)
        logging.info(f'{self.name} - Summary for member {name}')
        logging.info(f'{self.name} -    Emitted records             : {self.stats["rec"]}')
        return status
    # def lxmltext1(self, e):
    #     r = e.text.replace('\n','').replace('\r','').lstrip().rstrip() if type(e.text) == type('') else ''
    #     if not r and e.tag in  ['td', 'h3']:
    #         for x in e.itertext():
    #             if x != '':
    #                 r = x
    #                 break
    #     return r
    # def lxmltext2(self, e):
    #     return e.text_content().replace('\n','').replace('\r','').lstrip().rstrip()
    def lxmltext(self, e):
        return xxxx(e)
    def analyzexml(self, stream, name):
        status = Object()
        status.error = None        
        logging.trace(f'{self.name} - Analyzing xml stream {name}')
        self.context = ''
        self.stats = Counter()
        # try:
        #     page=fromstring(stream)
        #     self.lxmltext = self.lxmltext1
        # except:
        #     page=lxml.html.fromstring(stream)
        #     self.lxmltext = self.lxmltext2
        page=lxml.html.fromstring(stream)
        if "BEGIN" in self.contextrules:
            logging.trace(f'{self.name} - Calling BEGIN at pattern {self.stats["patterns"]}')
            self.contextrules["BEGIN"]["action"](self)
        for ln in page.getiterator():
            if self.context == 'BREAK': break
            self.stats['patterns'] += 1
            for t in self.rules:
                p = t.search(ln.tag)
                if not p: continue
                for r in self.rules[t]:
                    self.stats['ger'] += 1
                    p = r["regexp"].search(self.lxmltext(ln))
                    if not p: continue
                    self.stats['sger'] += 1
                    logging.trace(f'{self.name} - Calling {r["action"].__name__} at text {self.lxmltext(ln)} for tag: {ln.tag}')
                    r["action"](self, ln, p.group, name)
                    if self.context == 'BREAK': break
            if self.context == '':
                for t in self.outcontextrules:
                    p = t.search(ln.tag)
                    if not p: continue
                    for r in self.outcontextrules[t]:           
                        self.stats['oer'] += 1
                        p = r["regexp"].search(self.lxmltext(ln))
                        if not p: continue
                        self.stats['soer'] += 1
                        logging.trace(f'{self.name} - Calling {r["action"].__name__} at text {self.lxmltext(ln)} for tag: {ln.tag}')
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
                logging.trace(f'{self.name} - Calling {r["action"].__name__} at text {self.lxmltext(ln)} for tag: {ln.tag}')
                r["action"](self, ln, p.group, name)
        if "END" in self.contextrules:
            logging.trace(f'{self.name} - Calling END at pattern {self.stats["patterns"]}')
            self.contextrules["END"]["action"](self)
        logging.info(f'{self.name} - Summary for member {name}')
        logging.info(f'{self.name} -    Analyzed patterns           : {self.stats["patterns"]}')
        logging.info(f'{self.name} -    Evaluated rules (global)    : {self.stats["ger"]}')
        logging.info(f'{self.name} -    Satisfied rules (global)    : {self.stats["sger"]}')
        logging.info(f'{self.name} -    Evaluated rules (outcontext): {self.stats["oer"]}')
        logging.info(f'{self.name} -    Satisfied rules (outcontext): {self.stats["soer"]}')
        logging.info(f'{self.name} -    Evaluated rules (context)   : {self.stats["cer"]}')
        logging.info(f'{self.name} -    Satisfied rules (context)   : {self.stats["scer"]}')
        logging.info(f'{self.name} -    Emitted records             : {self.stats["rec"]}')

        return status
