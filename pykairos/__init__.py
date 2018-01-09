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
import string, random, ssl, logging, os, binascii, subprocess, zipfile, tarfile, bz2, shutil, re, json,  time, lxml.html, magic, cgi, sys, multiprocessing, pyinotify, urllib, base64, psycopg2, psycopg2.extras, psycopg2.extensions, queue, multiprocessing, multiprocessing.connection
from collections import *
from datetime import datetime
from aiohttp import web, WSCloseCode, WSMsgType, MultiDict
from urllib.parse import parse_qs

global kairos
kairos=dict()

def ficon (node):
    icon_file = "fa fa-folder btnn"
    icon_opened = "fa fa-folder-open btnn"
    icon_closed = "fa fa-folder btnn"
    if node['icon'] == 'T':
        icon_file = "fa fa-trash btnt"
        icon_opened = "fa fa-trash-o btnt"
        icon_closed = "fa fa-trash btnt"
    if node['icon'] == 'B':
        icon_file = "fa fa-folder btnb"
        icon_opened = "fa fa-folder-open btnb"
        icon_closed = "fa fa-folder btnb"
    if node['icon'] == 'A':
        icon_file = "fa fa-folder btna"
        icon_opened = "fa fa-folder-open btna"
        icon_closed = "fa fa-folder btna"
    if node['icon'] == 'C':
        icon_file = "fa fa-folder btnc"
        icon_opened = "fa fa-folder-open btnc"
        icon_closed = "fa fa-folder btnc"
    if node['icon'] == 'L':
        icon_file = "fa fa-folder btnl"
        icon_opened = "fa fa-folder-open btnl"
        icon_closed = "fa fa-folder btnl"
    if node['icon'] == 'D':
        icon_file = "fa fa-database btnd"
        icon_opened = "fa fa-database btnd"
        icon_closed = "fa fa-database btnd"
    return (icon_file, icon_opened, icon_closed)

def replaceeval(obj, recursive=False):
    if not recursive:
        for e in obj:
            obj[e] = replaceeval(obj[e], recursive=True)
    if type(obj) == type('a'):
        try: obj = obj % kairos
        except: pass
    elif type(obj) == type([]):
        i=0
        for e in obj:
            obj[i] = replaceeval(e, recursive=True)
            i+=1
    elif type(obj) == type({}):
        for e in obj:
            obj[e] = replaceeval(obj[e], recursive=True)
    else: pass
    return obj
        
def trace_call(func):
    def wrapper(*args, **kwargs):
        logging.debug('>>> Entering %s ...' % func.__name__)
        response = func(*args, **kwargs)
        logging.debug('<<< Leaving %s ...' % func.__name__)
        return response
    return wrapper

def intercept_logging_and_internal_error(func):
    def wrapper(*args, **kwargs):
        request = args[1]
        params = parse_qs(request.query_string)
        if 'logging' in params:
            logger = logging.getLogger()
            if params['logging'][0] == 'debug': logger.setLevel(logging.DEBUG)
            if params['logging'][0] == 'info': logger.setLevel(logging.INFO)
            if params['logging'][0] == 'warn': logger.setLevel(logging.WARNING)
            if params['logging'][0] == 'error': logger.setLevel(logging.ERROR)
            if params['logging'][0] == 'fatal': logger.setLevel(logging.CRITICAL)
        try:
            response = func(*args, **kwargs)
            return response
        except:
            tb = sys.exc_info()
            #message = "Kairos internal error!"
            logging.error(str(tb))
            #logging.critical(message)
            message = str(tb[1])
            #logging.critical(message)
            return web.json_response(dict(success=False, message=message))
            #raise
    return wrapper

class Object: pass


class Parallel:
    def __init__(s, action, workers=multiprocessing.cpu_count()):
        s.limit = int(workers)
        s.workers = dict()
        s.action = action
    def push(s, arg):
        if len(s.workers.keys()) < s.limit:
            p = multiprocessing.Process(target=s.action, args=(arg,))
            p.start()
            s.workers[p.sentinel] = p
        else:
            if len(s.workers.keys()) == s.limit:
                x = multiprocessing.connection.wait(s.workers.keys())
                for e in x:
                    s.workers[e].join()
                    del s.workers[e]
                p = multiprocessing.Process(target=s.action, args=(arg,))
                p.start()
                s.workers[p.sentinel] = p
    def join(s):
        while len(s.workers):
            x = multiprocessing.connection.wait(s.workers.keys())
            for e in x:
                s.workers[e].join()
                del s.workers[e]

class Cache:
    def __init__(s,database=None, autocommit=False, objects=False, schema=None):
            agensstr = "host='localhost' user='agensgraph' dbname='" + database + "'" if database != None else "host='localhost' user='agensgraph'"
            s.agens = psycopg2.connect(agensstr)
            s.autocommit = autocommit
            s.schema = schema
            if autocommit: s.agens.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            if schema: s.execute("set search_path = " + schema)
            if objects: s.execute("set graph_path = kairos")       
    def execute(s,*req):
        logging.debug('Executing request: ' + req[0])
        c = s.agens.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        c.execute(*req)
        logging.debug('Request completed!')
        return c
    def disconnect(s):
        if not s.autocommit: s.agens.commit()
        s.agens.close()

class Arcfile:
    def __init__(s,file,mode='r'):
        opmode=mode.split(':')
        s.type='tarfile'
        if opmode[0] in ['r','a']:
            if not zipfile.is_zipfile(file) and not tarfile.is_tarfile(file): raise TypeError
            if zipfile.is_zipfile(file):
                s.archive=zipfile.ZipFile(file,mode)
                s.type='zipfile'
            else: s.archive=tarfile.open(file,mode)
        else:
            if len(opmode)>1 and opmode[1] in ['zip']:
                s.type='zipfile'
                s.archive=zipfile.ZipFile(file,opmode[0],zipfile.ZIP_DEFLATED)
            else: s.archive=tarfile.open(file,mode)
    def close(s):
        return s.archive.close()
    def list(s):
        if s.type=='tarfile': return s.archive.getnames()
        else: return s.archive.namelist()
    def read(s,member):
        if s.type=='tarfile':
            try: return bz2.decompress(s.archive.extractfile(s.archive.getmember(member).name).read())
            except: return s.archive.extractfile(s.archive.getmember(member).name).read()
        else:
            try: return bz2.decompress(s.archive.read(member))
            except: return s.archive.read(member)
    def write(s,member,stream):
        if s.type=='tarfile':
            inf=tarfile.TarInfo()
            inf.name=member
            inf.size=len(stream)
            inf.mtime = time.time()
            return s.archive.addfile(inf,StringIO.StringIO(stream))
        else: return s.archive.writestr(member,stream)

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
        logging.debug(s.name + ' - Init Analyzer()')
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
    def debug(s, m):
        logging.debug(s.name + ' - ' +m)
    def addRule(s, r):
        logging.debug(s.name + ' - Adding rule, regular expression: /' + r["regexp"] + '/, action: ' + r["action"].__name__)
        if 'tag' in r: s.rules.append({"action": r["action"], "regexp": re.compile(r["regexp"]), "tag": re.compile(r["tag"])})
        else: s.rules.append({"action": r["action"], "regexp": re.compile(r["regexp"])})
    def addOutContextRule(s, r):
        logging.debug(s.name + ' - Adding out context rule, regular expression: /' + r["regexp"] + '/, action: ' + r["action"].__name__)
        if 'tag' in r: s.outcontextrules.append({"action": r["action"], "regexp": re.compile(r["regexp"]), "tag": re.compile(r["tag"])})
        else: s.outcontextrules.append({"action": r["action"], "regexp": re.compile(r["regexp"])})
    def addContextRule(s, r):
        logging.debug(s.name + ' - Adding context rule, context: ' + r["context"] + ', regular expression: /' + r["regexp"] + '/, action: ' + r["action"].__name__)
        if 'tag' in r: s.contextrules[r["context"]] = {"action": r["action"], "regexp": re.compile(r["regexp"]), "tag": re.compile(r["tag"])}
        else: s.contextrules[r["context"]] = {"action": r["action"], "regexp": re.compile(r["regexp"])}
    def setContext(s, c):
        logging.debug(s.name + ' - Setting context: ' + c)
        s.context = c
    def emit(s, col, d, v):
        s.stats["rec"] += 1
        s.listener(col, d, v, s.listenercontext)
        s.gcpt += 1;
        logging.debug(json.dumps(d))
    def analyze(s, stream, name):
        logging.debug(s.name + ' - Scope: ' + str(s.scope))
        if "content" in s.configurator and s.configurator["content"] == "xml": s.analyzexml(stream.decode(), name)
        elif "content" in s.configurator and s.configurator["content"] == "json": s.analyzejson(stream.decode(), name)
        else: s.analyzestr(stream.decode(errors="ignore"), name)
    def analyzestr(s, stream, name):
        logging.debug(s.name + ' - Analyzing stream ' + name)
        s.context = ''
        s.stats = dict(lines=0, ger=0, sger=0, cer=0, scer=0, oer=0, soer=0, rec=0)
        if "BEGIN" in s.contextrules:
            logging.debug(s.name + ' - Calling BEGIN at line ' + str(s.stats["lines"]))
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
                logging.debug(s.name + ' - Calling ' + r["action"].__name__ + ' at line ' + str(s.stats["lines"]) + ' containing: |' + ln + '|')
                r["action"](s, ln, p.group, name)
            if s.context == '':
                for r in s.outcontextrules:
                    s.stats['oer'] += 1
                    p = r["regexp"].search(ln)
                    if not p: continue
                    s.stats['soer'] += 1
                    logging.debug(s.name + ' - Calling ' + r["action"].__name__ + ' at line ' + str(s.stats["lines"]) + ' containing: |' + ln + '|')
                    r["action"](s, ln, p.group, name)
                    break
            if s.context in s.contextrules:
                r = s.contextrules[s.context]
                s.stats['cer'] += 1
                p = r["regexp"].search(ln)
                if not p: continue
                s.stats['scer'] += 1
                logging.debug(s.name + ' - Calling ' + r["action"].__name__ + ' at line ' + str(s.stats["lines"]) + ' containing: |' + ln + '|')
                r["action"](s, ln, p.group, name)
        if "END" in s.contextrules:
            logging.debug(s.name + ' - Calling END at line ' + str(s.stats["lines"]))
            s.contextrules["END"]["action"](s)
        logging.info(s.name + ' - Summary for member ' + name);
        logging.info(s.name + ' -    Analyzed lines              : ' + str(s.stats["lines"]))
        logging.info(s.name + ' -    Evaluated rules (global)    : ' + str(s.stats["ger"]))
        logging.info(s.name + ' -    Satisfied rules (global)    : ' + str(s.stats["sger"]))
        logging.info(s.name + ' -    Evaluated rules (outcontext): ' + str(s.stats["oer"]))
        logging.info(s.name + ' -    Satisfied rules (outcontext): ' + str(s.stats["soer"]))
        logging.info(s.name + ' -    Evaluated rules (context)   : ' + str(s.stats["cer"]))
        logging.info(s.name + ' -    Satisfied rules (context)   : ' + str(s.stats["scer"]))
        logging.info(s.name + ' -    Emitted records             : ' + str(s.stats["rec"]))
    def analyzejson(s, stream, name):
        logging.debug(s.name + ' - Analyzing stream' + name)
        s.stats = dict(lines=0, er=0, ser=0, rec=0)
        d = json.loads(stream)
        for x in d['data']: s.emit(d['collection'], d['desc'], x)
        logging.debug(s.name + ' - Summary for member ' + name);
        logging.debug(s.name + ' -    Emitted records  : ' + str(s.stats["rec"]))
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
        logging.debug(s.name + ' - Analyzing xml stream' + name)
        s.context = ''
        s.stats = dict(patterns=0, ger=0, sger=0, cer=0, scer=0, oer=0, soer=0, rec=0)
        try:
            page=fromstring(stream)
            s.lxmltext = s.lxmltext1
        except:
            page=lxml.html.fromstring(stream)
            s.lxmltext = s.lxmltext2
        if "BEGIN" in s.contextrules:
            logging.debug(s.name + ' - Calling BEGIN at pattern ' + str(s.stats["patterns"]))
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
                logging.debug(s.name + ' - Calling ' + r["action"].__name__ + ' at text ' + s.lxmltext(ln) + ' for tag: ' + ln.tag)
                r["action"](s, ln, p.group, name)
                if s.context == 'BREAK': break
            if s.context == '':
                #for r in s.outcontextrules[0:1]:
                for r in s.outcontextrules:
                    s.stats['oer'] += 1
                    p = r["tag"].search(ln.tag)
                    if not p: continue
                    p = r["regexp"].search(s.lxmltext(ln))
                    if not p: continue
                    #s.outcontextrules = s.outcontextrules[1:]
                    s.stats['soer'] += 1
                    logging.debug(s.name + ' - Calling ' + r["action"].__name__ + ' at text ' + s.lxmltext(ln) + ' for tag: ' + ln.tag)
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
                logging.debug(s.name + ' - Calling ' + r["action"].__name__ + ' at text ' + s.lxmltext(ln) + ' for tag: ' + ln.tag)
                r["action"](s, ln, p.group, name)
        if "END" in s.contextrules:
            logging.debug(s.name + ' - Calling END at pattern ' + str(s.stats["patterns"]))
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

        
class NotifyEventHandler(pyinotify.ProcessEvent):
    
    def process_default(s, event):
        logging.debug('from process_default: ' + str(event))
        
    def process_IN_CREATE(s, event):
        if event.path == '/autoupload' and event.maskname == 'IN_CREATE|IN_ISDIR' and event.dir:
            logging.info('Watching a new directory: ' + event.pathname + ' ...')
            s.wm.add_watch(event.pathname, pyinotify.ALL_EVENTS)
        
    def process_IN_MODIFY(s, event):
        if 'kairos_' in event.path and not event.dir and os.path.isfile(event.pathname):
            if os.path.basename(event.pathname)[0] != '.':
                logging.info("Uploading file '" + event.pathname + "' into database " + os.path.basename(event.path) + " ...")
                status = os.system('kairos -s uploadnode --nodesdb ' + os.path.basename(event.path) + ' --file ' + event.pathname)
                if status == 0: os.remove(event.pathname)
                logging.info("File '" + event.pathname + "' has been uploaded to " + os.path.basename(event.path) + "!")
    def process_IN_ATTRIB(s, event):
        s.process_IN_MODIFY(event)
        
class KairosNotifier:
    def __init__(s):
        logging.info('Init notification process...')
        s.wm = pyinotify.WatchManager()
        s.wm.add_watch('/autoupload', pyinotify.ALL_EVENTS)
        logging.info('Watching directory: /autoupload ...')
        for d in os.listdir('/autoupload'):
            wdir = '/autoupload/' + d
            if 'kairos_' in d and os.path.isdir(wdir):
                logging.info('Watching directory: ' + wdir + ' ...')
                s.wm.add_watch(wdir, pyinotify.ALL_EVENTS)
                for f in os.listdir(wdir): os.system('touch ' + wdir + '/' +f)
        s.eh = NotifyEventHandler()
        s.eh.wm = s.wm
        s.notifier = pyinotify.Notifier(s.wm, s.eh)
        import setproctitle
        multiprocessing.current_process().name = 'NotifyProcess'
        logging.info('Starting notification process...')
        setproctitle.setproctitle('KairosNotifier')
        logging.info('Process name: ' + setproctitle.getproctitle())
        logging.info('Process id: ' + str(os.getpid()))
        s.notifier.loop()
    
class KairosWorker:
    def __init__(s, jpypeflag=True):
        
        # if jpypeflag:
        #     jarpath = os.environ['CLASSPATH']
        #     jvm = jpype.getDefaultJVMPath()
        #     jpype.startJVM(jvm, '-Djava.class.path=' + jarpath)

        app = web.Application()
        app['websockets'] = []

        @trace_call
        def on_shutdown(app):
            for ws in app['websockets']:
                ws.close(code=WSCloseCode.GOING_AWAY, message='Server shutdown')

        app.on_shutdown.append(on_shutdown)

        app.router.add_get('/', s.file_index)
        app.router.add_get('/index.html', s.file_index)
        app.router.add_get('/charter.js', s.file_charter)
        app.router.add_get('/client.js', s.file_client)
        app.router.add_get('/checkserverconfig', s.checkserverconfig)
        app.router.add_get('/createsystem', s.createsystem)
        app.router.add_get('/getsettings', s.getsettings)
        app.router.add_get('/getmenus', s.getmenus)
        app.router.add_get('/gettree', s.gettree)
        app.router.add_get('/getnode', s.getnode)
        app.router.add_get('/getchart', s.getchart)
        app.router.add_get('/getjsonobject', s.getjsonobject)
        app.router.add_get('/getchoice', s.getchoice)
        app.router.add_get('/getlayout', s.getlayout)
        app.router.add_get('/gettemplate', s.gettemplate)
        app.router.add_get('/getcolors', s.getcolors)
        app.router.add_get('/getqueries', s.getqueries)
        app.router.add_get('/getcharts', s.getcharts)
        app.router.add_get('/getchoices', s.getchoices)
        app.router.add_get('/getobject', s.getobject)
        app.router.add_get('/executequery', s.executequery)
        app.router.add_get('/getmemberlist', s.getmemberlist)
        app.router.add_get('/getcollections', s.getcollections)
        app.router.add_get('/getmember', s.getmember)
        app.router.add_get('/buildallcollectioncaches', s.buildallcollectioncaches)
        app.router.add_get('/buildcollectioncache', s.buildcollectioncache)
        app.router.add_get('/clearcollectioncache', s.clearcollectioncache)
        app.router.add_get('/dropcollectioncache', s.dropcollectioncache)
        app.router.add_get('/displaycollection', s.displaycollection)
        app.router.add_get('/createnode', s.createnode)
        app.router.add_get('/renamenode', s.renamenode)
        app.router.add_get('/deletenode', s.deletenode)
        app.router.add_get('/movenode', s.movenode)
        app.router.add_get('/emptytrash', s.emptytrash)
        app.router.add_get('/checkwallpaper', s.checkwallpaper)
        app.router.add_get('/listdatabases', s.listdatabases)
        app.router.add_get('/listroles', s.listroles)
        app.router.add_get('/listusers', s.listusers)
        app.router.add_get('/listgrants', s.listgrants)
        app.router.add_get('/listsystemdb', s.listsystemdb)
        app.router.add_get('/listnodesdb', s.listnodesdb)
        app.router.add_get('/listtemplates', s.listtemplates)
        app.router.add_get('/listaggregators', s.listaggregators)
        app.router.add_get('/listliveobjects', s.listliveobjects)
        app.router.add_get('/listwallpapers', s.listwallpapers)
        app.router.add_get('/listcolors', s.listcolors)
        app.router.add_get('/listobjects', s.listobjects)
        app.router.add_get('/createrole', s.createrole)
        app.router.add_get('/createuser', s.createuser)
        app.router.add_get('/creategrant', s.creategrant)
        app.router.add_get('/deleterole', s.deleterole)
        app.router.add_get('/deleteuser', s.deleteuser)
        app.router.add_get('/resetpassword', s.resetpassword)
        app.router.add_get('/deletegrant', s.deletegrant)
        app.router.add_get('/updatesettings', s.updatesettings)
        app.router.add_get('/get_kairos_log', s.websocket_handler)
        app.router.add_get('/get_webserver_log', s.websocket_handler)
        app.router.add_get('/get_postgres_logfile', s.websocket_handler)
        app.router.add_get('/deleteobject', s.deleteobject)
        app.router.add_get('/downloadobject', s.downloadobject)
        app.router.add_get('/downloadsource', s.downloadsource)
        app.router.add_get('/getBchildren', s.getBchildren)
        app.router.add_get('/unload', s.unload)
        app.router.add_get('/compareaddnode', s.compareaddnode)
        app.router.add_get('/aggregateaddnode', s.aggregateaddnode)
        app.router.add_get('/linkfathernode', s.linkfathernode)
        app.router.add_get('/applyaggregator', s.applyaggregator)
        app.router.add_get('/applyliveobject', s.applyliveobject)
        app.router.add_get('/uploadnode', s.uploadnode)
        app.router.add_get('/uploadobject', s.uploadobject)
        app.router.add_get('/getid', s.getid)
        app.router.add_post('/changepassword', s.changepassword)
        app.router.add_post('/uploadobject', s.uploadobject)
        app.router.add_post('/setobject', s.setobject)
        app.router.add_post('/checkuserpassword', s.checkuserpassword)
        app.router.add_post('/uploadnode', s.uploadnode)
        app.router.add_static('/resources/', path='/kairos/resources', name='resources')
        s.application = app
        logging.basicConfig(format='%(asctime)s %(process)5s %(levelname)8s %(message)s', level=logging.INFO, filename="/var/log/kairos/kairos.log")
        import setproctitle
        setproctitle.setproctitle('KairosWorker')
        logging.info('Process name: ' + setproctitle.getproctitle())
        logging.info('Process id: ' + str(os.getpid()))

    @trace_call
    async def websocket_handler(s, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        request.app['websockets'].append(ws)
        try:
            async for msg in ws:
                if msg.type == WSMsgType.TEXT:
                    logging.debug('Got request : ' + msg.data)
                    alpha = subprocess.Popen(msg.data,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
                    line = alpha.stdout.readline()
                    while line:
                        ws.send_str(line.decode())
                        line = alpha.stdout.readline()
                    ws.send_str('__END_OF_PIPE__')
                    await ws.close()
                elif msg.type == WSMsgType.ERROR:
                    logging.error('Unexpected error, ws connection closed with exception %s' % ws.exception())
        finally:
            request.app['websockets'].remove(ws)
        return ws

    def file_index(s, request):
        return web.Response(content_type='text/html', text=open('/kairos/index.html').read())

    def file_charter(s, request):
        return web.Response(content_type='application/octet-stream', text=open('/kairos/charter.js').read())

    def file_client(s, request):
        return web.Response(content_type='application/octet-stream', text=open('/kairos/client.js').read())
        
    @trace_call
    def ideletecollection(s, nid, collection=None, nodesdb=None):
        cache = s.igetcache(nid, nodesdb=nodesdb)
        if hasattr(cache, 'rid'):
            rid = cache.rid
            collections = cache.collections
            if collection in collections:
                hcache = Cache(cache.database, schema=cache.name)
                hcache.execute("drop table if exists " + collection)
                hcache.disconnect()
                del collections[collection]
                ncache = Cache(nodesdb, objects=True)
                ncache.execute("match (c:caches) where id(c) = '" + rid + "' set c.collections = '" + json.dumps(collections) + "'")
                ncache.disconnect()
        
    @trace_call
    def ideletecache(s, nid, nodesdb=None):
        ncache = Cache(nodesdb, autocommit=True, objects=True)
        x = ncache.execute("match (n:nodes)-[:node_has_cache]->(c:caches) where id(n) = '" + nid + "' return id(c) as cid")
        cids = [row['cid'] for row in x.fetchall()]
        if len(cids):
            cid = cids[0]
            y = ncache.execute("match (c:caches) where id(c) = '" + cid + "' return c.name as name")
            schname = [row['name'] for row in y.fetchall()][0]
            ncache.execute("drop schema " + schname + " cascade")
            ncache.execute("match (c:caches) where id(c) = '" + cid + "' detach delete c")
        ncache.disconnect()
        
    @trace_call
    def ideletesource(s, nid, nodesdb=None):
        ncache = Cache(nodesdb, objects=True)
        x = ncache.execute("match (n:nodes)-[:node_has_source]->(s:sources) where id(n) = '" + nid + "' return id(s) as sid")
        sids = [row['sid'] for row in x.fetchall()]
        if len(sids):
            sid = sids[0]
            y = ncache.execute("match (s:sources) where id(s) = '" + sid + "' return s.location as location")
            location = [row['location'] for row in y.fetchall()][0]
            try: os.unlink(location)
            except: pass
            ncache.execute("match (s:sources) where id(s) = '" + sid + "' detach delete s")
        ncache.disconnect()

    @trace_call
    def icreatecache(s, nid, nodesdb=None):
        ncache = Cache(nodesdb, autocommit=True, objects=True)
        schname = 'cache_' + nid.replace('.', '_')
        ncache.execute("create schema " + schname)
        ncache.execute("match (n:nodes) where id(n) = '" + nid + "' create ((n)-[:node_has_cache]->(c:caches {created:now(), database:'" + nodesdb + "', name:'" + schname + "', queries:'" + json.dumps(dict()) + "', collections:'" + json.dumps(dict()) + "'}))")
        ncache.disconnect()
        
    @trace_call
    def icreatesource(s, nid, nodesdb=None, systemdb=None, stream=None, filename=None):
        filepath = '/files/' + nodesdb + '/' + nid + '.zip'
        infile = Arcfile(stream, 'r')
        ziparchive = Arcfile(filepath, 'w:zip')
        for m in infile.list(): ziparchive.write(m, infile.read(m))
        ziparchive.close()
        collections = dict()
        def listener(col, d, v, n):
            for x in v['collections']:
                if x not in collections: collections[x] = dict(analyzer=v['analyzer'],members=[])
                collections[x]['members'].append(v['member'])
        analmain = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'ANALMAIN', type:'analyzer'}")[0]
        analyzer = Analyzer(analmain, {}, listener, None)
        def do(member):
            logging.info('Analyzing member: ' + member + '...')
            analyzer.analyze(ziparchive.read(member), member)
            return None
        logging.info('Analyzing archive: ' + filepath + '...')
        ziparchive = Arcfile(filepath, 'r')
        for member in ziparchive.list(): do(member)
        ziparchive.close()
        ncache = Cache(nodesdb, objects=True)        
        ncache.execute("match (n:nodes) where id(n) = '" + nid + "' create ((n)-[:node_has_source]->(s:sources {created:now(), location: '" + filepath+ "', collections:'" + json.dumps(collections) + "'}))")
        ncache.execute("match (n:nodes) where id(n) = '" + nid + "' set n.type=to_json('B'::text), n.icon=to_json('B'::text)")
        ncache.disconnect()
        
    @trace_call
    def igetcache(s, nid, nodesdb=None):
        ncache = Cache(nodesdb, objects=True)
        x = ncache.execute("match (n:nodes)-[:node_has_cache]->(c:caches) where id(n) = '" + nid + "' return id(c) as rid, c.database as database, c.name as name, c.queries as queries, to_char(cast(c.created as timestamp), 'YYYY-MM-DD HH24:MI:SS.MS') as created, c.collections as collections")
        r = Object()
        for rx in x.fetchall():
            r.rid = rx['rid']
            r.database = rx['database']
            r.name = rx['name']
            r.queries = json.loads(rx['queries'])
            r.created = rx['created']
            r.collections = json.loads(rx['collections'])
        ncache.disconnect()
        return r
        
    @trace_call
    def igetsource(s, nid, nodesdb=None):
        ncache = Cache(nodesdb, objects=True)        
        x = ncache.execute("match (n:nodes)-[:node_has_source]->(s:sources) where id(n) = '" + nid + "' return id(s) as rid, s.location as location, to_char(cast(s.created as timestamp), 'YYYY-MM-DD HH24:MI:SS.MS') as created, s.collections as collections")
        r = Object()
        for rx in x.fetchall():
            r.rid = rx['rid']
            r.location = rx['location']
            r.created = rx['created']
            r.collections = json.loads(rx['collections'])
        ncache.disconnect()
        return r

    @trace_call
    def icreatesystem(s):
        ncache = Cache(None, autocommit=True)        
        x = ncache.execute("select datname from pg_database")
        databases = [row['datname'] for row in x.fetchall()]
        if 'kairos_system_system' in databases:
            ncache.disconnect()
            return
        logging.info("Creating a new kairos_system_system database...")
        ncache.execute("create database kairos_system_system with encoding 'utf8'")
        ncache.disconnect()
        ag = subprocess.run(['su', '-', 'agensgraph', '-c', 'agens -d kairos_system_system < /usr/local/src/kairos_system_system.sql'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if  ag.returncode: 
            logging.error('Error when trying to import data in kairos_system_system!')
            ncache = Cache('kairos_system_system')        
            ncache.execute("create graph kairos")
            ncache.execute("create vlabel objects")
            ncache.disconnect()
            logging.info("kairos_system_system database created.")
        else: logging.info("kairos_system_system database created and populated.")

    @trace_call
    def icreaterole(s, role=None):
        curdatabase = "kairos_group_" + role
        ncache = Cache(None, autocommit=True)        
        x = ncache.execute("select datname from pg_database")
        databases = [row['datname'] for row in x.fetchall()]
        if curdatabase in databases: return dict(success=False, message=user + ' role already exists!')
        logging.info("Creating a new " + curdatabase + " database ...")
        ncache.execute("create database kairos_group_" + role + " with encoding 'utf8'")
        logging.info(curdatabase + " database created.")
        ncache.execute("create role " + role)
        logging.info(role + " role created.")
        ncache.disconnect()
        ncache = Cache("kairos_group_" + role)        
        ncache.execute("create language plpythonu")
        ncache.execute("create extension oracle_fdw")
        ncache.execute("create graph kairos")
        ncache.execute("create vlabel objects")
        ncache.execute("create vlabel nodes")
        ncache.execute("create (:nodes {name:'/', type:'N', created:now(), status:'ACTIVE', icon:'N'})")
        ncache.execute("create (:nodes {name:'Trash', type:'T', created:now(), status:'DELETED', icon:'T'})")
        ncache.execute("create elabel node_has_children")
        ncache.execute("match (r:nodes {name:'/'}), (t:nodes {name:'Trash'}) create ((r)-[:node_has_children]->(t))") 
        ncache.execute("create elabel node_has_source")
        ncache.execute("create elabel node_has_cache")
        ncache.execute("create vlabel sources")
        ncache.execute("create vlabel caches")
        ncache.disconnect()        
        try: shutil.rmtree('/files/' + curdatabase)
        except: pass
        try: shutil.rmtree('/autoupload/' + curdatabase)
        except: pass
        os.mkdir('/files/' + curdatabase)
        os.mkdir('/autoupload/' + curdatabase)
        logging.info(curdatabase + " database created.")
        return dict(success=True, data=dict(msg=role + " role has been successfully created!"))

    @trace_call
    def icreateuser(s, user=None):
        curdatabase = "kairos_user_" + user
        ncache = Cache(None, autocommit=True)
        x = ncache.execute("select datname from pg_database")
        databases = [row['datname'] for row in x.fetchall()]
        if curdatabase in databases: return dict(success=False, message=user + ' user already exists!')
        logging.info("Creating a new " + curdatabase + " database ...")
        ncache.execute("create database kairos_user_" + user + " with encoding 'utf8'")
        logging.info(curdatabase + " database created.")
        ncache.execute("create user " + user + " password '" + user + "'")
        logging.info(user + " user created.")
        ncache.disconnect()
        ncache = Cache("kairos_user_" + user)
        ncache.execute("create language plpythonu")
        ncache.execute("create extension oracle_fdw")
        ncache.execute("create graph kairos")
        ncache.execute("create vlabel settings")
        ncache.execute("create (:settings {colors:'COLORS', keycode:0, logging:'info', loglines:100, nodesdb:'kairos_user_" + user + "', plotorientation:'horizontal', systemdb:'kairos_system_system', template:'DEFAULT', top:15, wallpaper:'DEFAULT'})")
        ncache.execute("create vlabel objects")
        ncache.execute("create vlabel nodes")
        ncache.execute("create (:nodes {name:'/', type:'N', created:now(), status:'ACTIVE', icon:'N'})")
        ncache.execute("create (:nodes {name:'Trash', type:'T', created:now(), status:'DELETED', icon:'T'})")
        ncache.execute("create elabel node_has_children")
        ncache.execute("match (r:nodes {name:'/'}), (t:nodes {name:'Trash'}) create ((r)-[:node_has_children]->(t))") 
        ncache.execute("create elabel node_has_source")
        ncache.execute("create elabel node_has_cache")
        ncache.execute("create vlabel sources")
        ncache.execute("create vlabel caches")
        ncache.disconnect()        
        try: shutil.rmtree('/files/' + curdatabase)
        except: pass
        try: shutil.rmtree('/autoupload/' + curdatabase)
        except: pass
        os.mkdir('/files/' + curdatabase)
        os.mkdir('/autoupload/' + curdatabase)
        logging.info(curdatabase + " database created.")
        return dict(success=True, data=dict(msg=user + " user has been successfully created!"))

    @trace_call
    def icreategrant(s, user=None, role=None):
        ncache = Cache(None)
        x = ncache.execute("select datname from pg_database")
        databases = [row['datname'] for row in x.fetchall()]
        dbgroup = "kairos_group_" + role
        dbuser = "kairos_user_" + user
        if dbgroup not in databases:
            ncache.disconnect()        
            return dict(success=False, message=role + " role doesn't exist!")
        if dbuser not in databases: 
            ncache.disconnect()        
            return dict(success=False, message=user + " user doesn't exist!")
        x = ncache.execute("select groname,usename from pg_group,pg_user where usesysid = any(grolist) and groname='" + role + "' and usename='" + user + "'")
        if len([row for row in x.fetchall()]) > 0:
            ncache.disconnect()        
            return dict(success=False, message=user + " user is already granted with " + role + " role!")
        for row in x.fetchall():
            data.append(dict(_id=row['usename'] + ':' + row['groname'], user=row['usename'], role=row['groname']))
        ncache.execute("grant " + role + " to " + user)
        ncache.disconnect()        
        return dict(success=True, data=dict(msg=role + " role has been successfully granted to " + user + " user!"))

    @trace_call
    def ideleterole(s, role=None):
        dbgroup = "kairos_group_" + role
        logging.info("Dropping " + dbgroup + " database...")
        ncache = Cache(None, autocommit=True)
        ncache.execute("drop database " + dbgroup)
        ncache.execute("drop role " + role)
        ncache.disconnect()              
        shutil.rmtree('/files/' + dbgroup)
        logging.info(dbgroup + " database removed.")
        return dict(success=True, data=dict(msg=role + " role has been successfully removed!"))

    @trace_call
    def ideleteuser(s, user=None):
        if user=='admin': return dict(success=False, message='admin user cannot be removed!')
        dbuser = "kairos_user_" + user
        logging.info("Dropping " + dbuser + " database...")
        ncache = Cache(None, autocommit=True)
        ncache.execute("drop database " + dbuser)
        ncache.execute("drop user " + user)
        shutil.rmtree('/files/' + dbuser)
        logging.info(dbuser + " database removed.")
        return dict(success=True, data=dict(msg=user + " user has been successfully removed!"))

    @trace_call
    def iresetpassword(s, user=None):
        if user=='admin': return dict(success=False, message='admin password cannot be reset!')
        dbuser = "kairos_user_" + user
        logging.info("Resetting " + user + " password...")
        ncache = Cache(None)
        ncache.execute("alter user " + user + " password '" + user + "'")
        ncache.disconnect()              
        logging.info(user + " password reset.")
        return dict(success=True, data=dict(msg=user + " password has been successfully reset!"))

    @trace_call
    def ideletegrant(s, role=None, user=None):
        ncache = Cache(None)
        ncache.execute("revoke " + role + " from " + user)
        ncache.disconnect()              
        return dict(success=True, data=dict(msg=user + " user has been successfully revoked from " + role + " role!"))

    @trace_call
    def ilistobjects(s, systemdb=None, nodesdb=None, where=''):
        data = []
        for db in [nodesdb, systemdb]:
            ncache = Cache(db, objects=True)
            y = ncache.execute("match (o:objects " + where + ") return id(o) as rid, o.id, o.type, to_char(cast(o.created as timestamp), 'YYYY-MM-DD HH24:MI:SS.MS') as created")
            for row in y.fetchall():
                item = dict()
                for x in row.keys(): item[x] = row[x]
                item['origin'] = db
                data.append(item)
            ncache.disconnect()              
        return data

    @trace_call
    def igetobjects(s, systemdb=None, nodesdb=None, where='', evalobject=True):
        data = []
        for db in [nodesdb, systemdb]:
            ncache = Cache(db, objects=True)
            x = ncache.execute("match (o:objects " + where + ") return o.filename, o.content, to_char(cast(o.created as timestamp), 'YYYY-MM-DD HH24:MI:SS.MS') as created")
            for row in x.fetchall():
                source = binascii.a2b_base64(row['content'])
                filename = row['filename']
                created = row['created']
                p = compile(source, filename, 'exec')
                global kairos
                locals()['kairos'] = kairos
                true = True
                false = False
                null = None
                exec(p, locals())
                obj = locals()['UserObject']()
                obj['origin'] = db
                obj['created'] = created
                if evalobject: obj = replaceeval(obj)
                data.append(obj)
            ncache.disconnect()              
        return data

    @trace_call
    def igetnodes(s, nodesdb=None, id=None, name=None, parent=None, root=False, child=None, countchildren=False, getsource=False, getcache=False):
        ncache = Cache(nodesdb, objects=True)
        selector = "id(n) as rid, n.type, n.name, n.icon, n.status, to_char(cast(n.created as timestamp), 'YYYY-MM-DD HH24:MI:SS.MS') as created, n.liveobject, n.aggregatorselector, n.aggregatorsort, n.aggregatortake, n.aggregatorskip, n.aggregatormethod, n.aggregatortimefilter, to_char(cast(n.aggregated as timestamp), 'YYYY-MM-DD HH24:MI:SS.MS') as aggregated, n.producers"
        if root: x = ncache.execute("match (n:nodes {name:'/'})-[:node_has_children]->(t:nodes {name:'Trash',status:'DELETED'}) return " + selector)
        if name and parent: x = ncache.execute("match (p:nodes)-[:node_has_children]->(n:nodes {name:'" + name + "'}) where id(p)='" + parent + "' return " + selector)
        if not name and parent: x = ncache.execute("match (p:nodes)-[:node_has_children]->(n:nodes) where id(p)='" + parent + "' return " + selector)
        if not name and child: x = ncache.execute("match (n:nodes)-[:node_has_children]->(c:nodes) where id(c)='" + child + "' return " + selector)
        if id: x = ncache.execute("match (n:nodes) where id(n)='" + id + "' return " + selector)
        selectednodes = [row for row in x.fetchall()]
        nodes=[]
        for row in selectednodes:
            node = dict(datasource=dict(cache=dict()))
            node['id'] = row['rid']
            node['name'] = row['name']
            node['icon'] = row['icon']
            node['status'] = row['status']
            node['created'] = row['created']
            node['datasource']['type'] = row['type']
            node['datasource']['producers'] = json.loads(row['producers']) if 'producers' in row  and row['producers'] else []
            if row['type'] in ['A', 'L']:
                node['datasource']['aggregated'] = row['aggregated'] if 'aggregated' in row and row['aggregated'] else None
                node['datasource']['aggregatorselector'] = row['aggregatorselector'] if 'aggregatorselector' in row and row['aggregatorselector'] else '/'
                node['datasource']['aggregatorsort'] = row['aggregatorsort'] if 'aggregatorsort' in row and row['aggregatorsort'] else 'desc'
                node['datasource']['aggregatortake'] = row['aggregatortake'] if 'aggregatortake' in row and row['aggregatortake'] else 1
                node['datasource']['aggregatorskip'] = row['aggregatorskip'] if 'aggregatorskip' in row and row['aggregatorskip'] else 0
                node['datasource']['aggregatormethod'] = row['aggregatormethod'] if 'aggregatormethod' in row and row['aggregatormethod'] else '$none'
                node['datasource']['aggregatortimefilter'] = row['aggregatortimefilter'] if 'aggregatortimefilter' in row and row['aggregatortimefilter'] else '.'
            if row['type'] in ['D']:
                node['datasource']['liveobject'] = row['liveobject']
                d = dict()
                try:
                    liveobject = s.igetobjects(nodesdb=nodesdb, systemdb='kairos_system_system', where="{id:'" + row['liveobject'] + "', type:'liveobject'}")[0]
                    for e in liveobject['tables']: d[e] = True
                except: pass
                node['datasource']['collections'] = d
            if countchildren:
                x = ncache.execute("select count(*) as count from (match (n:nodes)-[:node_has_children]->(c:nodes) where id(n)='" + node['id'] + "' return c) as foo")
                for r in x.fetchall():
                    node['kids'] = r['count']
            if getsource:
                if row['type'] == 'B':
                    source = s.igetsource(node['id'], nodesdb=nodesdb)
                    if hasattr(source, 'rid'):
                        node['datasource']['uploaded'] = source.created
                        node['datasource']['collections'] = source.collections
                        node['datasource']['location'] = source.location
                if row['type'] in ['A', 'C']:
                    try:
                        firstproducer = s.igetnodes(nodesdb=nodesdb, id=node['datasource']['producers'][0]['id'], getsource=True)[0]
                        node['datasource']['collections'] = firstproducer['datasource']['collections']
                    except: node['datasource']['collections'] = None
            if getcache:
                if row['type'] in ['A', 'B', 'D']:
                    cache = s.igetcache(node['id'], nodesdb=nodesdb)
                    if hasattr(cache, 'rid'):
                        node['datasource']['cache']['collections'] = cache.collections
                        node['datasource']['cache']['queries'] = cache.queries
                        node['datasource']['cache']['name'] = cache.name
                        node['datasource']['cache']['database'] = cache.database
            nodes.append(node)
        ncache.disconnect()              
        return nodes
    
    @trace_call
    def igetpath(s, nodesdb=None, id=None):
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        return '' if node['name'] == '/' else s.igetpath(nodesdb=nodesdb, id=s.igetnodes(nodesdb=nodesdb, child=id)[0]['id']) + '/' + node['name']

    @trace_call
    def icreatenode(s, nodesdb=None, id=None, name=None):
        ncache = Cache(nodesdb, objects=True)
        if not name:
            x = ncache.execute("select to_char(now(), 'YYYY-MM-DD HH24:MI:SS.MS') as name")
            for row in x.fetchall(): name = row['name']
        x = ncache.execute("match (p:nodes) where id(p)='" + id + "' create (p)-[:node_has_children]->(n:nodes {name:'" + name + "', type:'N', created:now(), status:'ACTIVE', icon:'N'}) return id(n) as rid") 
        for row in x.fetchall():
            rid = row['rid']
        ncache.disconnect()              
        return rid

    @trace_call
    def ideletenode(s, nodesdb=None, id=None):
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True)[0]
        root = s.igetnodes(nodesdb=nodesdb, root=True)[0]
        trash = s.igetnodes(nodesdb=nodesdb, parent=root['id'], name='Trash')[0]
        if root['id'] == node['id']: return 'Root node cannot be removed!'
        if node['datasource']['type'] == 'T': return 'A trash cannot be removed!'
        ncache = Cache(nodesdb, objects=True)
        if node['status'] == 'DELETED':
            x = ncache.execute("match (n:nodes)-[:node_has_children*]->(d:nodes) where id(n) = '" + id + "' return id(d) as rid")
            listnodes = [row['rid'] for row in x.fetchall()]
            listnodes.append(id)
            for rid in listnodes:
                s.ideletesource(rid, nodesdb=nodesdb)
                s.ideletecache(rid, nodesdb=nodesdb)
                ncache.execute("match (n:nodes) where id(n) = '" + rid + "' detach delete n") 
        else:
            ncache.execute("match (p:nodes)-[l:node_has_children]->(n:nodes) where id(n) = '" + id + "' detach delete l") 
            ncache.execute("match (t:nodes {name:'Trash'}), (n:nodes) where id(n) = '" + id + "' create (t)-[:node_has_children]->(n)") 
            x = ncache.execute("match (n:nodes)-[:node_has_children*]->(d:nodes) where id(n) = '" + id + "' return id(d) as rid") 
            listnodes = [row['rid'] for row in x.fetchall()]
            for rid in listnodes: ncache.execute("match (n:nodes) where id(n) = '" + rid + "' set n.status=to_json('DELETED'::text)")
            ncache.execute("match (n:nodes) where id(n) = '" + id + "' set n.status=to_json('DELETED'::text)")
        ncache.disconnect()              
        return None
    
    @trace_call
    def iapplyliveobject(s, id=None, cache=None, liveobject=None):
        hcache = Cache(cache.database, schema=cache.name)
        extension = liveobject['extension']
        server = liveobject['id']
        dbserver = liveobject['dbserver']
        hcache.execute('drop server if exists ' + server + ' cascade')
        hcache.execute('create server ' + server + ' foreign data wrapper ' + extension + " options (dbserver '" + dbserver + "')")
        hcache.execute('grant usage on foreign server ' + server + ' to agensgraph')
        user = liveobject['user']
        password = liveobject['password']
        hcache.execute('create user mapping for agensgraph server ' + server + " options (user '" + user + "', password '" + password + "')")
        collections = []
        message = None
        for t in liveobject['tables']:
            description = liveobject['tables'][t]['description']
            request = liveobject['tables'][t]['request']
            logging.debug('Foreign request: ' + request)
            desc = ", ".join(["%(k)s %(v)s" % dict(k=d, v=description[d]) for d in description])
            hcache.execute('create foreign table foreign_' + t + '(' + desc + ') server ' + server + " options (table '(" + request.replace("'", "''").replace('kairos_nodeid_to_be_replaced', id) + ")')")
            collections.append(t)
        hcache.disconnect()
        return (message, collections)

    @trace_call
    def icheckcolcachetypeA(s, node, cache=None, collections=None, nodesdb=None, systemdb=None):
        nid = node['id']
        ntype = node['datasource']['type']
        todo = dict()
        mapproducers = dict()
        datepart = dict()
        for collection in collections:
            mapproducers[collection] = dict(deleted=dict(), created=dict(), updated=dict(), unchanged=dict())
            datepart[collection] = dict()
            for part in cache.collections[collection]: mapproducers[collection]['deleted'][part] = dict(id=part)
        node = s.igetnodes(nodesdb=nodesdb, id=nid)[0]
        producers = s.iexpand(pattern=node['datasource']['aggregatorselector'], nodesdb=nodesdb, sort=node['datasource']['aggregatorsort'], skip=node['datasource']['aggregatorskip'], take=node['datasource']['aggregatortake'])
        ncache = Cache(nodesdb, objects=True)
        ncache.execute("match (n:nodes) where id(n) = '" + nid + "' set n.producers='" + json.dumps(producers) + "', n.aggregated=to_json(now())")
        ncache.disconnect()              
        for producer in node['datasource']['producers']:
            pid = producer['id']
            for collection in collections:        
                datepart[collection][pid] = cache.collections[collection][pid] if pid in cache.collections[collection] else None
                if pid in mapproducers[collection]['deleted']:
                    del mapproducers[collection]['deleted'][pid]
                    mapproducers[collection]['unchanged'][pid] = producer
                else: mapproducers[collection]['created'][pid] = producer
                if datepart[collection][pid] == None and pid in mapproducers[collection]['unchanged']:
                    del mapproducers[collection]['unchanged'][pid]
                    mapproducers[collection]['updated'][pid] = producer
            pnode = s.igetnodes(nodesdb=nodesdb, id=producer['id'], getsource=True, getcache=True)[0]
            pdone = s.ibuildcollectioncache(pnode, collections=collections, systemdb=systemdb, nodesdb=nodesdb)
            pcache = s.igetcache(pnode['id'], nodesdb=nodesdb)
            ptype = pnode['datasource']['type']
            for collection in collections:
                if pdone[collection] and pid in mapproducers[collection]['unchanged']:
                    del mapproducers[collection]['unchanged'][pid]
                    mapproducers[collection]['updated'][pid] = producer
                for p in pcache.collections[collection]:
                    if datepart[collection][pid] != None and pcache.collections[collection][p] > datepart[collection][pid] and pid in mapproducers[collection]['unchanged']:
                        del mapproducers[collection]['unchanged'][pid]
                        mapproducers[collection]['updated'][pid] = producer
                if ptype in 'D': mapproducers[collection]['updated'][pid] = producer
                todo[collection] = True if len(mapproducers[collection]['deleted']) + len(mapproducers[collection]['created']) + len(mapproducers[collection]['updated']) > 0 else False
        for collection in collections:
            message = "Node: " + nid + ", Type: " + ntype + ", Collection: '" + collection + "'"
            message += ", Producers: (Unchanged: "
            for x in mapproducers[collection]['unchanged']: message += str(x) + ','
            message += " Updated: "
            for x in mapproducers[collection]['updated']: message += str(x) + ','
            message += " New: "
            for x in mapproducers[collection]['created']: message += str(x) + ','
            message += " Deleted: "
            for x in mapproducers[collection]['deleted']: message += str(x) + ','
            message += ")"
            logging.info(message)
        return (todo, mapproducers)

    @trace_call
    def icheckcolcachetypeB(s, node, cache=None, collections=None, nodesdb=None, systemdb=None):
        todo = dict()
        analyzers = dict ()
        nid = node['id']
        ntype = node['datasource']['type']
        for collection in collections:
            logging.info("Node: " + nid + ", Type: " + ntype + ", checking collection cache: '" + collection + "' ...")
            todo[collection] = False
            analyzername = node ['datasource']['collections'][collection]['analyzer']
            analyzer = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'" + analyzername + "', type:'analyzer'}")[0]
            datepart = cache.collections[collection][nid] if collection in cache.collections and nid in cache.collections[collection] else None
            todo[collection] = True if datepart == None else todo[collection]
            todo[collection] = True if datepart != None and node['datasource']['uploaded'] > datepart else todo[collection]
            todo[collection] = True if datepart != None and analyzer['created'] > datepart else todo[collection]
            analyzers[collection] = analyzer
        return (todo, analyzers)

    @trace_call
    def icheckcolcachetypeD(s, node, cache=None, collections=None, nodesdb=None, systemdb=None):
        todo = dict()
        nid = node['id']
        ntype = node['datasource']['type']
        for collection in collections:
            logging.info("Node: " + nid + ", Type: " + ntype + ", checking collection cache: '" + collection + "' ...")
            todo[collection] = True        
        return todo

    @trace_call
    def idropcolcachetypeA(s, node, cache=None, collection=None, mapproducers=None):
        exclude = [str(x) for x in mapproducers[collection]['unchanged'].keys()]
        hcache = Cache(cache.database, schema=cache.name)
        if len(exclude) == 0: hcache.execute("drop table if exists " + collection)
        if len(exclude) == 1: hcache.execute("delete from " + collection + " where kairos_nodeid not in ('" + exclude[0] + "')")
        if len(exclude) > 1: hcache.execute("delete from " + collection + " where kairos_nodeid not in " + str(tuple(exclude)))
        hcache.disconnect()
        for x in mapproducers[collection]['deleted'] : del cache.collections[collection][x]

    @trace_call
    def idropcolcachetypeB(s, node, cache=None, collection=None):
        hcache = Cache(cache.database, schema=cache.name)
        hcache.execute("drop table if exists " + collection)
        hcache.disconnect()

    @trace_call
    def idropcolcachetypeD(s, node, cache=None, collection=None):
        pass
        # generator = lambda x=16, y=string.ascii_uppercase: ''.join(random.choice(y) for _ in range(x))
        # hcache = Cache(cache.database, schema=cache.name)
        # tbname = "TO_BE_DELETED_" + generator()
        # hcache.execute("alter table " + collection + " rename to " + tbname)
        # hcache.execute("create table " + collection + " as select * from " + tbname + " limit 0")
        # hcache.disconnect()

    @trace_call
    def idropcollectioncache(s, node, collection=None, nodesdb=None):
        nid = node['id']
        cache = s.igetcache(nid, nodesdb=nodesdb)
        hcache = Cache(cache.database, schema=cache.name)
        hcache.execute("drop table if exists " + collection)
        hcache.disconnect()
        del cache.collections[collection]
        ncache = Cache(nodesdb, objects=True)
        ncache.execute("match (c:caches) where id(c) = '" + cache.rid + "' set c.collections='" + json.dumps(cache.collections) + "'")
        ncache.disconnect()

    @trace_call
    def ibuildcolcachetypeA(s, node, cache=None, collection=None, mapproducers=None, nodesdb=None, systemdb=None):
        nid = node['id']
        ntype = node['datasource']['type']
        logging.info("Node: " + nid + ", Type: " + ntype + ", building new collection cache: '" + collection + "' ...")
        hcache = Cache(cache.database, schema=cache.name)
        function = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'" + node['datasource']['aggregatormethod'] + "', type:'aggregator'}")[0]
        meet = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id: 'meet', type: 'function'}")[0]
        hcache.execute(function["function"])
        hcache.execute(meet["function"])
        hcache.execute("drop table if exists aggregator")
        hcache.execute("create table aggregator as select '" + node['datasource']['aggregatormethod'] + "'::text as method")
        producers = list(mapproducers[collection]['updated'].keys())
        producers.extend(list(mapproducers[collection]['created'].keys()))
        for producer in producers:
            logging.info("Node: " + nid + ", Type: " + ntype + ", building partition for producer: '" + producer + "' ...")
            pnode = s.igetnodes(nodesdb=nodesdb, id=producer, getcache=True)[0]
            inschname = pnode['datasource']['cache']['name']
            x = hcache.execute("select distinct table_name from information_schema.columns where table_schema='" + cache.name + "'")
            schdesc = [row['table_name'] for row in x.fetchall()]
            x = hcache.execute("select distinct table_name from information_schema.columns where table_schema='" + inschname + "'")
            inschdesc = [row['table_name'] for row in x.fetchall()]
            if collection.lower() not in inschdesc: continue
            if collection.lower() not in schdesc: hcache.execute("create table " + collection.lower() + " as select * from " + inschname + "." + collection.lower() + " limit 0")
            tabledesc = OrderedDict()
            x = hcache.execute("select column_name, data_type from information_schema.columns where table_name = '" + collection.lower() + "' and table_schema = '" + cache.name + "'")
            for row in x.fetchall(): tabledesc[row['column_name']] = row['data_type']
            lgby = []
            lavg = []
            lsum = []
            where = ' '
            for k in tabledesc:
                if tabledesc[k]=='text': lgby.append(k)
                if tabledesc[k]=='integer': lsum.append(k)
                if tabledesc[k]=='bigint': lsum.append(k)
                if tabledesc[k]=='real': lavg.append(k)
            listf = []
            for x in lgby: listf.append(x)
            for x in lavg: listf.append(x)
            for x in lsum: listf.append(x)
            timestamp = True if 'timestamp' in lgby else False
            if timestamp:
                where = " where " + cache.name + ".meet(timestamp,'" + node['datasource']['aggregatortimefilter'] + "') or timestamp='00000000000000000'"
            subrequest = "select " + ",".join(listf) + " from " + inschname + "." + collection.lower() + where
            request = 'insert into ' + collection.lower() + '(' + ','.join(listf) + ') select '
            for x in lgby:
                if x=='timestamp': request += function["name"] + '(timestamp) as timestamp, '
                else: request += x + ', '
            for x in lavg:
                request += "avg(coalesce(" + x + ")) as " + x + ", "
            for x in lsum:
                request += 'sum(' + x + ') as ' + x + ', '
            request = request[:-2] + ' from (' + subrequest + ') as foo group by '
            for x in lgby: request = request + function["name"] + '(timestamp), ' if x == 'timestamp' else request + x + ', '
            request = request[:-2]
            hcache.execute(request)
            cache.collections[collection][pnode['id']] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        hcache.disconnect()

    @trace_call
    def ibuildcolcachetypeB(s, node, cache=None, collections=None, analyzers=None, nodesdb=None):
        nid = node['id']
        files = dict()
        lock = multiprocessing.Lock()
        for collection in collections:
            fname = '/ramdisk/' + cache.name + '_' + collection + '.sql'
            try: os.remove(fname)
            except: pass
        def listener(col, d, v, n):
            lock.acquire()
            fname = '/ramdisk/' + cache.name + '_' + col + '.sql'
            f = open(fname, 'a')
            if os.stat(fname).st_size == 0:
                f.write("SET statement_timeout = 0;\n")
                f.writelines("SET lock_timeout = 0;\n")
                f.write("SET idle_in_transaction_session_timeout = 0;\n")
                f.write("SET client_encoding = 'UTF8';\n")
                f.write("SET standard_conforming_strings = on;\n")
                f.write("SET check_function_bodies = false;\n")
                f.write("SET client_min_messages = warning;\n")
                f.write("SET row_security = off;\n")
                f.write("SET search_path = " + cache.name + ", pg_catalog;\n")
                f.write("SET default_tablespace = '';\n")
                f.write("SET default_with_oids = false;\n")
                d['kairos_nodeid'] = 'text'
                request = 'create table ' + col + '('
                l = sorted(d.keys())
                for k in l: request += k + ' ' + d[k] +  ', '
                request = request[:-2] + ');\n'
                f.write(request)
                f.write("alter table " + col + " owner to agensgraph;\n")
                request = 'copy ' + col + '('
                for k in l: request += k +  ', '
                request = request[:-2] + ') from stdin;\n'
                f.write(request)
            record = ''
            v['kairos_nodeid'] = nid
            for k in sorted(v.keys()): record += '\\N\t' if v[k] == '' else str(v[k]).replace('\t','\\t') + '\t'
            record = record[:-1] + '\n'
            f.write(record)
            f.close()
            lock.release()
        def nulllistener(col, d, v, n): pass
        members =dict()
        for collection in collections:
            for member in node['datasource']['collections'][collection]['members']:
                members[member]=analyzers[collection]
        source = node['datasource']['location']
        archive = Arcfile(source)
        logging.info('Analyzing archive: ' + source + '...')
        try: nolistener = eval(os.environ['NOLISTENER'])
        except: nolistener = False
        listen = nulllistener if nolistener else listener
        def do(member):
            if member in members:
                analyzer = Analyzer(members[member], set(collections), listen, nid)
                logging.info('Analyzing member: ' + member + '...')
                analyzer.analyze(archive.read(member), member)
                return None
        try: limit = int(os.environ['PARALLEL'])
        except: limit = 0
        limit = multiprocessing.cpu_count() if limit==0 else limit
        pl = Parallel(do, workers=limit)
        for e in archive.list(): pl.push(e)
        pl.join()
        archive.close()
        logging.info('Writing cache ...')
        def write(fname):
            logging.info('Writing collection from ' + fname + ' ...')
            f = open(fname, 'a')       
            f.write('\\.\n')
            f.close()
            ag = subprocess.run(['su', '-', 'agensgraph', '-c', 'psql -d ' + nodesdb + ' < ' + fname], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if  ag.returncode: 
                raise Exception('Error when trying to import data from ' + fname)
            else : 
                os.remove(fname)
        pl = Parallel(write, workers=limit)
        for collection in collections: pl.push('/ramdisk/' + cache.name + '_' + collection + '.sql')
        pl.join()
        for collection in collections: cache.collections[collection][nid] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    @trace_call
    def ibuildcolcachetypeD(s, node, cache=None, collection=None, liveobject=None):
        nid = node['id']
        ntype = node['datasource']['type']
        logging.info("Node: " + nid + ", Type: " + ntype + ", building new collection cache: '" + collection + "' ...")
        cache.collections[collection][nid] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    @trace_call
    def icheckcollectioncache(s, node, cache=None, collections=None, nodesdb=None, systemdb=None):
        todo = dict()
        mapproducers = dict()
        analyzers = dict()
        nid = node['id']
        ntype = node['datasource']['type']
        if ntype in ['C', 'L']:
            for producer in node['datasource']['producers']:
                pnode = s.igetnodes(nodesdb=nodesdb, id=producer['id'], getsource=True, getcache=True)[0]
                s.ibuildcollectioncache(pnode, collections=collections, systemdb=systemdb, nodesdb=nodesdb)
            for collection in collections: todo[collection] = False
        if ntype in ['A', 'B', 'D']:
            for collection in collections:
                if collection not in cache.collections: cache.collections[collection] = dict()
        if ntype in ['A']: (todo, mapproducers) = s.icheckcolcachetypeA(node, cache=cache, collections=collections, nodesdb=nodesdb, systemdb=systemdb)
        if ntype in ['B']: (todo, analyzers) = s.icheckcolcachetypeB(node, cache=cache, collections=collections, nodesdb=nodesdb, systemdb=systemdb)
        if ntype in ['D']: todo = s.icheckcolcachetypeD(node, cache=cache, collections=collections, nodesdb=nodesdb, systemdb=systemdb)
        return (todo, mapproducers, analyzers)

    @trace_call
    def ibuildcollectioncache(s, node, collections=None, nodesdb=None, systemdb=None):
        nid = node['id']
        ntype = node['datasource']['type']
        nodecache = node['datasource']['cache']
        if 'name' not in nodecache: s.icreatecache(nid, nodesdb=nodesdb)
        cache = s.igetcache(nid, nodesdb=nodesdb)
        if '*' in collections: collections = {k for k in node['datasource']['collections']}
        (todo, mapproducers, analyzers) = s.icheckcollectioncache(node, cache=cache, collections=collections, nodesdb=nodesdb, systemdb=systemdb)
        if True in todo.values():
            tcollections = [k for k in todo if todo[k]]
            logging.info("Node: " + nid + ", Type: " + ntype + ", building collection cache: '" + str(tcollections) + "' ...")
            dbname = cache.name
            for collection in tcollections:
                logging.info("Node: " + nid + ", Type: " + ntype + ", removing obsolete parts of old collection cache: '" + collection + "' ...")
                if ntype in ['A']: s.idropcolcachetypeA(node, mapproducers=mapproducers, cache=cache, collection=collection)
                if ntype in ['B']: s.idropcolcachetypeB(node, cache=cache, collection=collection)
                if ntype in ['D']: s.idropcolcachetypeD(node, cache=cache, collection=collection)                
            for collection in tcollections:
                if ntype in ['A']: s.ibuildcolcachetypeA(node, cache=cache, collection=collection, nodesdb=nodesdb, systemdb=systemdb, mapproducers=mapproducers)
                if ntype in ['D']:
                    liveobject = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'" + node['datasource']['liveobject'] + "', type:'liveobject'}")[0]
                    s.ibuildcolcachetypeD(node, cache=cache, collection=collection, liveobject=liveobject)
            if ntype in ['B']: s.ibuildcolcachetypeB(node, cache=cache, collections=tcollections, analyzers=analyzers, nodesdb=nodesdb)
            logging.info("Node: " + nid + ", Type: " + ntype + ", updating cache with collections info: '" + str(tcollections) + "' ...")
            ncache = Cache(nodesdb, objects=True)
            ncache.execute("match (n:nodes)-[:node_has_cache]->(c:caches) where id(n) = '" + nid + "' set c.collections = '" + json.dumps(cache.collections) + "'")
            ncache.disconnect()
        return todo
    
    @trace_call
    def ibuildquerycache(s, node, query=None, nodesdb=None, systemdb=None):
        nid = node['id']
        qid = query['id']
        ntype = node['datasource']['type']
        logging.info("Node: " + nid + ", Type: " + ntype + ", checking query cache: '" + qid + "' ...")
        cache = s.igetcache(nid, nodesdb=nodesdb)
        message = None
        if ntype in ['C', 'L']:
            for producer in node['datasource']['producers']:
                pnode = s.igetnodes(nodesdb=nodesdb, id=producer['id'], getsource=True, getcache=True)[0]
                message = s.ibuildquerycache(pnode, query=query, systemdb=systemdb, nodesdb=nodesdb)
                if message: return message
        if ntype in ['A', 'B', 'D']:
            todo = True if ntype in ['D'] else False
            todo = True if qid not in cache.queries else todo
            todo = True if "nocache" in query and query["nocache"] else todo
            for collection in query['collections']:
                for part in cache.collections[collection]:
                    todo = True if qid in cache.queries and cache.queries[qid] < cache.collections[collection][part] else todo
            if todo:
                hcache = Cache(cache.database, schema=cache.name)
                table = qid
                logging.info("Node: " + nid + ", Type: " + ntype + ", removing old query cache: '" + qid + "' ...")
                hcache.execute("drop table if exists " + table)
                logging.info("Node: " + nid + ", Type: " + ntype + ", building new query cache: '" + qid + "' ...")
                if 'userfunctions' in query:
                    for ufn in query['userfunctions']:
                        uf = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'" + ufn + "', type:'function'}")[0]
                        hcache.execute(uf["function"])
                global kairos
                kairos['node'] = node
                try: hcache.execute("create table " + table + " as select * from (" + query['request'] + ") as foo")
                except:
                    tb = sys.exc_info()
                    message = str(tb[1])
                    return message
                cache.queries[qid] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                hcache.disconnect()
                logging.info("Node: " + nid + ", Type: " + ntype + ", updating cache with query info: '" + qid + "' ...")
                ncache = Cache(nodesdb, objects=True)
                ncache.execute("match (n:nodes)-[:node_has_cache]->(c:caches) where id(n) = '" + nid + "' set c.queries = '" + json.dumps(cache.queries) + "'")
                ncache.disconnect()
            else:
                logging.info("Node: " + nid + ", Type: " + ntype + ", nothing to do for query cache: '" + qid + "' ...")
            return message
   
    @trace_call
    def iqueryexecute(s, node, query=None, nodesdb=None, limit=None):
        result = []
        nid = node['id']
        qid = query['id']
        ntype = node['datasource']['type']
        logging.info("Node: " + nid + ", Type: " + ntype + ", executing query: '" + qid + "' ...")
        cache = s.igetcache(nid, nodesdb=nodesdb)
        if ntype in ['C', 'L']:
            for producer in node['datasource']['producers']:
                pnode = s.igetnodes(nodesdb=nodesdb, id=producer['id'], getsource=True, getcache=True)[0]
                if ntype in ['L']: result = s.iqueryexecute(pnode, query=query, nodesdb=nodesdb, limit=limit)
                else: result.append(s.iqueryexecute(pnode, query=query, nodesdb=nodesdb, limit=limit))
        else:
            hcache = Cache(cache.database, schema=cache.name)
            table = qid
            if 'filterable' in query and query['filterable']:
                for x in hcache.execute("select * from " + table + " where label in (select label from (select label, sum(value) weight from " + table + " group by label order by weight desc limit " + str(limit) + ") as foo)"):
                    result.append(x)
            else:
                for x in hcache.execute("select * from " + table):
                    result.append(x)
            hcache.disconnect()
        return result
  
    @trace_call
    def iexpand(s, pattern=None, sort=None, nodesdb=None, skip=0, take=1):
        skip=int(skip)
        take=int(take)
        d=dict()
        for i in pattern.split('|'):
            nodes = s.igetnodes(nodesdb=nodesdb, root=True)
            for p in i.split('/')[1:]:
                newnodes = []
                for n in nodes:
                    children = s.igetnodes(nodesdb=nodesdb, parent=n['id'])
                    for e in children:
                        if re.match(p, e['name']): newnodes.append(e)
                nodes = newnodes
            for n in nodes: d[s.igetpath(nodesdb=nodesdb, id=n['id'])] = n['id']
        result = [dict(path=k, id=d[k]) for k in sorted(d.keys())] if sort != 'desc' else [dict(path=k, id=d[k]) for k in sorted(d.keys(), reverse=True)]
        return result[skip:skip+take]
                
    @intercept_logging_and_internal_error
    @trace_call
    def getid(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        pattern = params['pattern'][0]
        result = s.iexpand(pattern=pattern, nodesdb=nodesdb)
        return web.json_response(dict(success=True, data=result))
    
    @intercept_logging_and_internal_error
    @trace_call
    def checkserverconfig(s, request):
        s.icreatesystem()
        s.icreateuser(user="admin")
        return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    def createsystem(s, request):
        s.icreatesystem()
        return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    async def checkuserpassword(s, request):
        multipart = await request.post()
        params = parse_qs(request.query_string)
        user = multipart['user'] if 'user' in multipart else params['user'][0]
        password = multipart['password'] if 'password' in multipart else params['password'][0]
        adminrights = True if user == 'admin' else False
        agensstr = "host='localhost' dbname='kairos_user_" + user + "' user='" + user + "' password='" + password + "'"
        try: 
            agens = psycopg2.connect(agensstr)
            agens.close()
            return web.json_response(dict(success=True, data=dict(adminrights = adminrights)))
        except:
            message = "Invalid password!"
            logging.warning(message)
            return web.json_response(dict(success=False, message=message))

    @intercept_logging_and_internal_error
    @trace_call
    async def setobject(s, request):
        multipart = await request.post()
        params = parse_qs(request.query_string)
        database = multipart['database'] if 'database' in multipart else params['database'][0]
        source = multipart['source'] if 'source' in multipart else params['source'][0]
        try:
            p = compile(source, 'stream', 'exec')
            kairos = dict()
            true = True
            false = False
            null = None
            exec(p, locals())
            obj = locals()['UserObject']()
            typeobj = obj['type']
            id = obj['id']
            filename = id.lower() + '.py'
            content = binascii.b2a_base64(source.encode())
            ncache = Cache(database, objects=True)
            ncache.execute("match (o:objects {id:'" + id + "', type:'" + typeobj + "'}) detach delete (o)")
            ncache.execute("create (:objects {id:'" + id + "', type:'" + typeobj + "', created: now(), filename:'" + filename + "', content:'" + content.decode() + "'})")
            ncache.disconnect()
            return web.json_response(dict(success=True, data=dict(msg='Object: ' + id + ' of type: ' + typeobj + ' has been successfully saved!')))
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            return web.json_response(dict(success=False, message=message))


    @intercept_logging_and_internal_error
    @trace_call
    def getsettings(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        db = 'kairos_user_' + user
        ncache = Cache(db, objects=True)
        y = ncache.execute("match (s:settings) return cast(s.top as int) as top, s.colors, cast(s.keycode as int) as keycode, s.logging, s.nodesdb, cast(s.loglines as int) as loglines, s.systemdb, s.template, s.wallpaper, s.plotorientation")
        settings = dict()
        for row in y.fetchall():
            for x in row.keys(): settings[x] = row[x]
        ncache.disconnect()
        return web.json_response(dict(success=True, data=dict(settings=settings)))

    @intercept_logging_and_internal_error
    @trace_call
    def checkwallpaper(s, request):
        params = parse_qs(request.query_string)
        wallpaper = params['wallpaper'][0]
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        return web.json_response(dict(success=True, data="/resources/DEFAULT.jpg"))

    @intercept_logging_and_internal_error
    @trace_call
    def listdatabases(s, request):
        ncache = Cache()
        params = parse_qs(request.query_string)
        user = params['user'][0]
        adminrights = True if params['admin'][0] == "true" else False
        data = []
        x = ncache.execute("select datname, pg_database_size(datname) as size from pg_database where datname like 'kairos_%'")
        databases = {row['datname']:row['size'] for row in x.fetchall()}
        x = ncache.execute("select groname from pg_group,pg_user where usesysid = any(grolist) and usename='" + user + "'")
        groups = ['kairos_group_' + row['groname'] for row in x.fetchall()]
        ncache.disconnect()
        for k in databases:
            if adminrights:
                data.append(dict(name=k, size=databases[k] * 1.0 / 1024 / 1024))
            else:
                if k == 'kairos_user_' + user:
                    data.append(dict(name=k, size=databases[k] * 1.0 / 1024 / 1024))
                if 'kairos_group_' in k:
                    if k in groups:
                        data.append(dict(name=k, size=databases[k] * 1.0 / 1024 / 1024))
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listsystemdb(s, request):
        ncache = Cache()
        x = ncache.execute("select datname from pg_database")
        databases = [row['datname'] for row in x.fetchall()]
        ncache.disconnect()
        data = []
        for k in databases:
            if 'kairos_system_' in k: data.append(dict(name=k))
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listnodesdb(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        ncache = Cache()
        x = ncache.execute("select datname from pg_database")
        databases = [row['datname'] for row in x.fetchall()]
        x = ncache.execute("select groname from pg_group,pg_user where usesysid = any(grolist) and usename='" + user + "'")
        groupdb = ['kairos_group_' + row['groname'] for row in x.fetchall()]
        ncache.disconnect()
        data = []
        for k in databases:
            if k == 'kairos_user_' + user: data.append(dict(name=k))
            if k in groupdb: data.append(dict(name=k))
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listtemplates(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        data = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="{type:'template'}")
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listaggregators(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        data = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="{type:'aggregator'}")
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listliveobjects(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        data = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="{type:'liveobject'}")
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listwallpapers(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        data = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="{type:'wallpaper'}")
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listcolors(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        data = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="{type:'color'}")
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listobjects(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        data = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="")
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def getobject(s, request):
        params = parse_qs(request.query_string)
        database = params['database'][0]
        objtype = params['type'][0]
        objid = params['id'][0]
        ncache = Cache(database, objects=True)
        y = ncache.execute("match (o:objects {id:'" + objid + "', type:'" + objtype + "'}) return o.content")
        result = dict()
        for row in y.fetchall():
            for x in row.keys(): result[x] = row[x]
        ncache.disconnect()
        source = binascii.a2b_base64(result['content'])
        return web.json_response(dict(success=True, data=source.decode()))

    @intercept_logging_and_internal_error
    @trace_call
    def updatesettings(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        loglines = params['loglines'][0]
        template = params['template'][0]
        colors = params['colors'][0]
        wallpaper = params['wallpaper'][0]
        top = params['top'][0]
        keycode = params['keycode'][0]
        plotorientation = params['plotorientation'][0]
        logging = params['logging'][0]
        db = "kairos_user_" + user
        ncache = Cache(db, objects=True)       
        ncache.execute("match (s:settings) detach delete (s)")
        ncache.execute("create (:settings {colors:'" + colors + "', keycode:" + keycode + ", logging:'" + logging + "', loglines:" + loglines + ", nodesdb:'" + nodesdb + "', plotorientation:'" + plotorientation + "', systemdb:'" + systemdb + "', template:'" + template + "', top:" + top + ", wallpaper:'" + wallpaper + "'})")
        ncache.disconnect()
        return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    async def uploadobject(s, request):
        params = parse_qs(request.query_string)
        if 'mode' in params:
            mode = params['mode'][0]
            if mode == 'conf':
                return web.json_response(dict(success=True, maxFileSize=2147483648))
        multipart = await request.post()
        upload = multipart['file']
        nodesdb = multipart['nodesdb'] if 'nodesdb' in multipart else params['nodesdb'][0]
        filename = upload.filename
        content = upload.file.read()
        uploadtype = upload.content_type
        if uploadtype == 'image/jpeg':
            typeobj = 'wallpaper'
            id = filename.replace('.jpg', '')
        else:
            p = compile(content, filename, 'exec')
            kairos = dict()
            true = True
            false = False
            null = None
            exec(p, locals())
            obj = locals()['UserObject']()
            typeobj = obj['type']
            id = obj['id']
        content = binascii.b2a_base64(content)
        ncache = Cache(nodesdb, objects=True)
        ncache.execute("match (o:objects {id:'" + id + "', type:'" + typeobj + "'}) detach delete (o)")
        ncache.execute("create (:objects {id:'" + id + "', type:'" + typeobj + "', created: now(), filename:'" + filename + "', content:'" + content.decode() + "'})")
        ncache.disconnect()
        return web.json_response(dict(success=True, state=True, name=filename))

    @intercept_logging_and_internal_error
    @trace_call
    async def uploadnode(s, request):
        params = parse_qs(request.query_string)
        if 'mode' in params:
            mode = params['mode'][0]
            if mode == 'conf':
                return web.json_response(dict(success=True, maxFileSize=2147483648))
        multipart = await request.post()
        upload = multipart['file']
        nodesdb = multipart['nodesdb'] if 'nodesdb' in multipart else params['nodesdb'][0]
        systemdb = multipart['systemdb'] if 'systemdb' in multipart else params['systemdb'][0]
        id = multipart['id'] if 'id' in multipart else params['id'][0] if 'id' in params else None
        filename = urllib.parse.unquote(upload.filename)
        node = s.igetnodes(nodesdb=nodesdb, root=True)[0] if id == None else s.igetnodes(nodesdb=nodesdb, id=id)[0]
        (base, ext) = os.path.splitext(filename)
        while ext != '': (base, ext) = os.path.splitext(base)
        nodes = base.split('_')
        for d in nodes:
            lnode = s.igetnodes(nodesdb=nodesdb, parent=node['id'], name=d)
            if len(lnode) == 0:
                child = s.icreatenode(nodesdb, id=node['id'], name=d)
                node = s.igetnodes(nodesdb=nodesdb, id=child)[0]
            else:
                node = lnode[0]
        id = node['id']
        s.ideletesource(id, nodesdb=nodesdb)
        s.icreatesource(id, nodesdb=nodesdb, systemdb=systemdb, stream=upload.file)
        return web.json_response(dict(success=True, state=True, name=filename))

    @intercept_logging_and_internal_error
    @trace_call
    def listroles(s, request):
        ncache = Cache()
        x = ncache.execute("select datname from pg_database")
        databases = [row['datname'] for row in x.fetchall()]
        ncache.disconnect()
        data = []
        for k in databases:
            if 'kairos_group_' in k:
                role = k.replace('kairos_group_','')
                data.append(dict(_id=role, role=role))
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listusers(s, request):
        ncache = Cache()
        x = ncache.execute("select datname from pg_database")
        databases = [row['datname'] for row in x.fetchall()]
        ncache.disconnect()
        data = []
        for k in databases:
            if 'kairos_user_' in k:
                user = k.replace('kairos_user_','')
                data.append(dict(_id=user, user=user))
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listgrants(s, request):
        ncache = Cache()
        x = ncache.execute("select groname,usename from pg_group,pg_user where usesysid = any(grolist)")
        data = []
        for row in x.fetchall():
            data.append(dict(_id=row['usename'] + ':' + row['groname'], user=row['usename'], role=row['groname']))
        ncache.disconnect()
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def createrole(s, request):
        params = parse_qs(request.query_string)
        role = params['role'][0]
        response = s.icreaterole(role=role)
        return web.json_response(response)

    @intercept_logging_and_internal_error
    @trace_call
    def createuser(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        response = s.icreateuser(user=user)
        return web.json_response(response)

    @intercept_logging_and_internal_error
    @trace_call
    def creategrant(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        role = params['role'][0]
        response = s.icreategrant(user=user,role=role)
        return web.json_response(response)

    @intercept_logging_and_internal_error
    @trace_call
    def deleterole(s, request):
        params = parse_qs(request.query_string)
        role = params['role'][0]
        response = s.ideleterole(role=role)
        return web.json_response(response)

    @intercept_logging_and_internal_error
    @trace_call
    def deleteuser(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        response = s.ideleteuser(user=user)
        return web.json_response(response)

    @intercept_logging_and_internal_error
    @trace_call
    def resetpassword(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        response = s.iresetpassword(user=user)
        return web.json_response(response)

    @intercept_logging_and_internal_error
    @trace_call
    def deletegrant(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        role = params['role'][0]
        response = s.ideletegrant(user=user,role=role)
        return web.json_response(response)

    @intercept_logging_and_internal_error
    @trace_call
    async def changepassword(s, request):
        multipart = await request.post()
        params = parse_qs(request.query_string)
        user = multipart['user'] if 'user' in multipart else params['user'][0]
        password = multipart['password'] if 'password' in multipart else params['password'][0]
        new = multipart['new'] if 'new' in multipart else params['new'][0]
        agensstr = "host='localhost' dbname='kairos_user_" + user + "' user='" + user + "' password='" + password + "'"
        try: 
            agens = psycopg2.connect(agensstr)
            agens.close()
        except:
            message = "Invalid password!"
            logging.warning(message)
            return web.json_response(dict(success=False, message=message))
        ncache = Cache()
        ncache.execute("alter user " + user + " password '" + new + "'")
        ncache.disconnect()
        return web.json_response(dict(success=True, data=dict(msg='Password has been successfully updated!')))

    @intercept_logging_and_internal_error
    @trace_call
    def deleteobject(s, request):
        params = parse_qs(request.query_string)
        database = params['database'][0]
        if 'kairos_system_' in database:
            message = 'A system object cannot be deleted!'
            return web.json_response(dict(success=False, status='error', message=message))
        id = params['id'][0]
        typeobj = params['type'][0]
        ncache = Cache(database, objects=True)
        ncache.execute("match (o:objects {id:'" + id + "', type:'" + typeobj + "'}) detach delete (o)")
        ncache.disconnect()
        return web.json_response(dict(success=True, data=dict(msg=id + ' ' + typeobj + ' object has been successfully removed!')))

    @intercept_logging_and_internal_error
    @trace_call
    def downloadobject(s, request):
        params = parse_qs(request.query_string)
        database = params['database'][0]
        id = params['id'][0]
        typeobj = params['type'][0]
        ncache = Cache(database, objects=True)
        y = ncache.execute("match (o:objects {id:'" + id + "', type:'" + typeobj + "'}) return o.filename, o.content")
        result = dict()
        for row in y.fetchall():
            for x in row.keys(): result[x] = row[x]
        ncache.disconnect()
        stream = binascii.a2b_base64(result['content'])
        return web.Response(headers=MultiDict({'Content-Disposition': 'Attachment;filename="' + result['filename'] + '"'}), body=stream)

    @intercept_logging_and_internal_error
    @trace_call
    def downloadsource(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True)[0]
        location = node['datasource']['location']
        filename = s.igetpath(nodesdb=nodesdb, id=id)[1:].replace('/','_')+'.zip'
        stream = open(location, 'rb').read()
        return web.Response(headers=MultiDict({'Content-Disposition': 'Attachment;filename="' + filename + '"'}), body=stream)

    @intercept_logging_and_internal_error
    @trace_call
    def getBchildren(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        list = []
        ncache = Cache(nodesdb, objects=True)
        x = ncache.execute("match (n:nodes)-[:node_has_children]->(c:nodes {type: to_json('B')}) where id(n) = '" + id + "' return id(c) as rid")
        list = [row['rid'] for row in x.fetchall()]
        return web.json_response(dict(success=True, data=list))

    @intercept_logging_and_internal_error
    @trace_call
    def getmemberlist(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True)[0]
        archive = Arcfile(node['datasource']['location'])
        list = []
        for member in archive.list(): list.append(dict(label=member))
        archive.close()
        return web.json_response(dict(success=True, data=list))

    @intercept_logging_and_internal_error
    @trace_call
    def getcollections(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True)[0]
        list = []
        if node['datasource']['type'] == 'D':
            loname = node['datasource']['liveobject']
            liveobject = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'" + loname + "', type:'liveobject'}")[0]
            for t in liveobject['tables']: list.append(dict(label=t))
        else:
            for collection in node['datasource']['collections']: list.append(dict(label=collection))
        return web.json_response(dict(success=True, data=list))

    @intercept_logging_and_internal_error
    @trace_call
    def getmember(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        member = params['member'][0]
        id = params['id'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True)[0]
        archive = Arcfile(node['datasource']['location'], 'r')
        stream = archive.read(member)
        type = magic.from_buffer(stream)
        stream = stream.decode().replace('#=', '# =').replace('#+', '# +')
        if 'html' in type.lower(): html = stream
        elif 'text' in type.lower(): html = '<pre>' + cgi.escape(stream) + '</pre>'
        else: html = 'Not yet taken into account'
        archive.close()
        return web.json_response(dict(success=True, data=html))

    @intercept_logging_and_internal_error
    @trace_call
    def getmenus(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        data = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{type:'menu'}")
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def gettree(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        parent = params['id'][0]
        root = True if parent == '0' else False
        ftype = lambda x: x['icon']
        if root:
            root = s.igetnodes(nodesdb=nodesdb, root=True)[0]
            (icon_file, icon_opened, icon_closed) = ficon(root)
            result = [dict(kids=True, id=root['id'].replace('#',''), text='/', userdata=dict(type=ftype(root)), icons=dict(file=icon_file, folder_opened=icon_opened, folder_closed=icon_closed))]
        else:
            children = []
            getkey = lambda x: x['text']
            for node in s.igetnodes(nodesdb=nodesdb, parent=parent, countchildren=True):
                (icon_file, icon_opened, icon_closed) = ficon(node)
                kids = True if node['kids'] > 0 else False
                children.append(dict(kids=kids, id=node['id'].replace('#',''), text=node['name'], userdata=dict(type=ftype(node)), icons=dict(file=icon_file, folder_opened=icon_opened, folder_closed=icon_closed)))
            result = [dict(id=parent, items=sorted(children, key=getkey))]
        return web.json_response(result)

    @intercept_logging_and_internal_error
    @trace_call
    def getnode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True)[0]
        return web.json_response(dict(success=True, data=node))

    @intercept_logging_and_internal_error
    @trace_call
    def createnode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        child = s.icreatenode(nodesdb=nodesdb, id=id)
        node = s.igetnodes(nodesdb=nodesdb, id=child)[0]
        return web.json_response(dict(success=True, data=node))

    @intercept_logging_and_internal_error
    @trace_call
    def renamenode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        new = params['new'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        root = s.igetnodes(nodesdb=nodesdb, root=True)[0]
        if root['id'] == node['id']:
            message = 'Root node cannot be renamed!'
            return web.json_response(dict(success=False, status='error', message=message))
        if node['datasource']['type'] == 'T':
            message = 'A trash cannot be renamed!'
            return web.json_response(dict(success=False, status='error', message=message))
        ncache = Cache(nodesdb, objects=True)
        x = ncache.execute("match (p:nodes)-[:node_has_children]->(n:nodes) where id(n) = '" + id + "' return id(p) as pid")
        parent=[row['pid'] for row in x.fetchall()][0]
        x = s.igetnodes(nodesdb=nodesdb, parent=parent, name=new)
        if len(x):
            message = new + " name already exists for parent: " + x[0]['name']
            ncache.disconnect()
            return web.json_response(dict(success=False, status='error', message=message))
        ncache.execute("match (n:nodes) where id(n) = '" + id + "' set n.name=to_json('" + new + "'::text)")
        ncache.disconnect()
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        return web.json_response(dict(success=True, data=node))

    @intercept_logging_and_internal_error
    @trace_call
    def deletenode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        message = s.ideletenode(id=id, nodesdb=nodesdb)
        if message: return web.json_response(dict(success=False, status='error', message=message))
        else: return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    def emptytrash(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        root = s.igetnodes(nodesdb=nodesdb, root=True)[0]
        trash = s.igetnodes(nodesdb=nodesdb, parent=root['id'], name='Trash')[0]
        ncache = Cache(nodesdb, objects=True)
        x = ncache.execute("match (t:nodes)-[:node_has_children*]->(d:nodes) where id(t) = '" + trash['id'] + "' return id(d) as rid")
        listnodes = [row['rid'] for row in x.fetchall()]
        for rid in listnodes:
            s.ideletesource(rid, nodesdb=nodesdb)
            s.ideletecache(rid, nodesdb=nodesdb)
            ncache.execute("match (n:nodes) where id(n) = '" + rid + "' detach delete n") 
        ncache.disconnect()
        return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    def movenode(s, request):
        params = parse_qs(request.query_string)
        origindb = params['origindb'][0]
        targetdb = params['targetdb'][0]
        pfrom = params['from'][0]
        pto = params['to'][0]
        fromnode = s.igetnodes(nodesdb=origindb, id=pfrom)[0]
        if fromnode['datasource']['type'] == 'T':
            message = 'A trash cannot be moved!'
            return web.json_response(dict(success=False, status='error', message=message))
        tonode = s.igetnodes(nodesdb=targetdb, id=pto)[0]
        ncache = Cache(targetdb, objects=True)
        ncache.execute("match (a:nodes)-[r:node_has_children]->(f:nodes) where id(f) = '" + pfrom + "' detach delete r") 
        ncache.execute("match (t:nodes), (f:nodes) where id(f) = '" + pfrom + "' and id(t) = '" + pto + "' create ((t)-[:node_has_children]->(f))")
        x = ncache.execute("match (n:nodes) where id(n) = '" + pto+ "' return n.status as status")
        status = [row['status'] for row in x.fetchall()][0]
        ncache.execute("match (t:nodes)-[:node_has_children*]->(d:nodes) where id(t) = '" + pfrom + "' set d.status=to_json('" + status + "'::text)")
        ncache.disconnect()
        node = s.igetnodes(nodesdb=targetdb, id=pfrom)[0]
        return web.json_response(dict(success=True, data=node))

    @intercept_logging_and_internal_error
    @trace_call
    def getchart(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        chart = params['chart'][0]
        variables = json.loads(params['variables'][0])
        global kairos
        for v in variables: kairos[v] = variables[v]
        chart = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'" + chart + "', type:'chart'}")[0]
        return web.json_response(dict(success=True, data=chart))

    @intercept_logging_and_internal_error
    @trace_call
    def getjsonobject(s, request):
        params = parse_qs(request.query_string)
        database = params['database'][0]
        id = params['id'][0]
        type = params['type'][0]
        obj = s.igetobjects(nodesdb=database, systemdb=database, where="{id:'" + id + "', type:'" + type + "'}", evalobject=False)[0]
        return web.json_response(dict(success=True, data=obj))
    
    @intercept_logging_and_internal_error
    @trace_call
    def getlayout(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        layout = params['layout'][0]
        variables = json.loads(params['variables'][0])
        global kairos
        for v in variables: kairos[v] = variables[v]
        layout = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'" + layout + "', type:'layout'}")[0]
        return web.json_response(dict(success=True, data=layout))
    
    @intercept_logging_and_internal_error
    @trace_call
    def getchoice(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        choice = params['choice'][0]
        variables = json.loads(params['variables'][0])
        global kairos
        for v in variables: kairos[v] = variables[v]
        choice = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'" + choice + "', type:'choice'}")[0]
        return web.json_response(dict(success=True, data=choice))

    @intercept_logging_and_internal_error
    @trace_call
    def gettemplate(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        template = params['template'][0]
        template = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'" + template + "', type:'template'}")[0]
        return web.json_response(dict(success=True, data=template))

    @intercept_logging_and_internal_error
    @trace_call
    def getcolors(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        colors = params['colors'][0]
        colors = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'" + colors + "', type:'color'}")[0]
        return web.json_response(dict(success=True, data=colors))

    @intercept_logging_and_internal_error
    @trace_call
    def getqueries(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        queries = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="{type:'query'}")
        return web.json_response(dict(success=True, data=queries))

    @intercept_logging_and_internal_error
    @trace_call
    def getcharts(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        charts = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="{type:'chart'}")
        return web.json_response(dict(success=True, data=charts))

    @intercept_logging_and_internal_error
    @trace_call
    def getchoices(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        choices = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="{type:'choice'}")
        return web.json_response(dict(success=True, data=choices))

    @intercept_logging_and_internal_error
    @trace_call
    def executequery(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        query = params['query'][0]
        limit = int(params['top'][0])
        id = params['id'][0]
        variables = json.loads(params['variables'][0])
        for v in variables: kairos[v] = variables[v]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True)[0]
        query = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'" + query + "', type:'query'}")[0]
        s.ibuildcollectioncache(node, collections=query['collections'], systemdb=systemdb, nodesdb=nodesdb)
        message = s.ibuildquerycache(node, query=query, systemdb=systemdb, nodesdb=nodesdb)
        if not message: result = s.iqueryexecute(node, query=query, nodesdb=nodesdb, limit=limit)
        if message:
            return web.json_response(dict(success=False, status='error', message=message))
        else:
            return web.json_response(dict(success=True, data=result))

    @intercept_logging_and_internal_error
    @trace_call
    def displaycollection(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        collection = params['collection'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True)[0]
        s.ibuildcollectioncache(node, collections=[collection], systemdb=systemdb, nodesdb=nodesdb)
        result = s.iqueryexecute(node, query=dict(id=collection), nodesdb=nodesdb)
        return web.json_response(dict(success=True, data=result))

    @intercept_logging_and_internal_error
    @trace_call
    def buildcollectioncache(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        collection = params['collection'][0]
        id = params['id'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True)[0]
        s.ibuildcollectioncache(node, collections={collection}, systemdb=systemdb, nodesdb=nodesdb)
        return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    def buildallcollectioncaches(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True)[0]
        s.ibuildcollectioncache(node, collections={'*'}, systemdb=systemdb, nodesdb=nodesdb)
        return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    def clearcollectioncache(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        s.ideletecache(id, nodesdb=nodesdb)
        return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    def dropcollectioncache(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0] 
        collection = params['collection'][0] 
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        s.idropcollectioncache(node, collection=collection, nodesdb=nodesdb)
        return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    def compareaddnode(s, request):
        params = parse_qs(request.query_string)
        origindb = params['origindb'][0]
        targetdb = params['targetdb'][0]
        fromid = params['from'][0]
        toid = params['to'][0]
        fnode = s.igetnodes(nodesdb=origindb, id=fromid)[0]
        tnode = s.igetnodes(nodesdb=targetdb, id=toid)[0]
        if fnode['status'] == 'DELETED' or tnode['status'] == 'DELETED':
            message = 'A deleted element cannot be part of a compare operation!'
            return web.json_response(dict(success=False, status='error', message=message))
        if fromid in tnode['datasource']['producers']:
            message = fromid + ": this node is already included in the list of producers!"
            return web.json_response(dict(success=False, status='error', message=message))
        producers = tnode['datasource']['producers']
        producers.append(dict(path=s.igetpath(nodesdb=origindb, id=fromid), id=fromid))
        ncache = Cache(targetdb, objects=True)
        ncache.execute("match (n:nodes) where id(n) = '" + toid+ "' set n.type=to_json('C'::text), n.icon=to_json('C'::text), n.producers = '" + json.dumps(producers) + "'")
        ncache.disconnect()
        tnode = s.igetnodes(nodesdb=targetdb, id=toid, getsource=True)[0]
        return web.json_response(dict(success=True, data=tnode))
    
    @intercept_logging_and_internal_error
    @trace_call
    def aggregateaddnode(s, request):
        params = parse_qs(request.query_string)
        origindb = params['origindb'][0]
        targetdb = params['targetdb'][0]
        fromid = params['from'][0]
        toid = params['to'][0]
        fnode = s.igetnodes(nodesdb=origindb, id=fromid)[0]
        tnode = s.igetnodes(nodesdb=targetdb, id=toid)[0]
        if fnode['status'] == 'DELETED' or tnode['status'] == 'DELETED':
            message = 'A deleted element cannot be part of an aggreagte operation!'
            return web.json_response(dict(success=False, status='error', message=message))
        if fromid in tnode['datasource']['producers']:
            message = fromid + ": this node is already included in the list of producers!"
            return web.json_response(dict(success=False, status='error', message=message))
        producers = tnode['datasource']['producers']
        producers.append(dict(path=s.igetpath(nodesdb=origindb, id=fromid), id=fromid))
        ncache = Cache(targetdb, objects=True)
        if 'aggregatorselector' not in tnode['datasource']:
            ncache.execute("match (n:nodes) where id(n) = '" + toid+ "' set n.type=to_json('A'::text), n.icon=to_json('A'::text), n.producers='" + json.dumps(producers) + "', n.aggregated=to_json(now()), n.aggregatorselector=to_json('" + s.igetpath(nodesdb=origindb, id=fromid) + '$' + "'::text), n.aggregatortake=to_json(1), n.aggregatortimefilter=to_json('.'::text), n.aggregatorskip=to_json(0), n.aggregatorsort=to_json('desc'::text), n.aggregatormethod=to_json('$none'::text)")
        else:
            ncache.execute("match (n:nodes) where id(n) = '" + toid+ "' set n.producers='" + json.dumps(producers) + "', n.aggregated=to_json(now()), n.aggregatorselector=to_json('" + tnode['datasource']['aggregatorselector'] + '|' + s.igetpath(nodesdb=origindb, id=fromid) + '$' + "'::text), n.aggregatortake=to_json(" + str(tnode['datasource']['aggregatortake'] +  1) + "")            
        ncache.disconnect()
        tnode = s.igetnodes(nodesdb=targetdb, id=toid, getsource=True)[0]
        return web.json_response(dict(success=True, data=tnode))
    
    @intercept_logging_and_internal_error
    @trace_call
    def applyaggregator(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        aggregatorselector = params['aggregatorselector'][0]
        aggregatortake = int(params['aggregatortake'][0])
        aggregatorskip = int(params['aggregatorskip'][0])
        aggregatortimefilter = params['aggregatortimefilter'][0]
        aggregatorsort = params['aggregatorsort'][0]
        aggregatormethod = params['aggregatormethod'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        if node['datasource']['type'] in ['A']:
            if node['datasource']['aggregatormethod'] != aggregatormethod or node['datasource']['aggregatortimefilter'] != aggregatortimefilter:
                logging.info("Node: " + id + ", Type: " + node['datasource']['type'] + ", deleting cache ...")
                s.ideletecache(id, nodesdb=nodesdb)
        if node['datasource']['type'] in ['A', 'N']:  
            producers = s.iexpand(pattern=aggregatorselector, nodesdb=nodesdb, sort=aggregatorsort, take=aggregatortake, skip=aggregatorskip)
            ncache = Cache(nodesdb, objects=True)
            ncache.execute("match (n:nodes) where id(n) = '" + id+ "' set n.type=to_json('A'::text), n.icon=to_json('A'::text), n.producers='" + json.dumps(producers) + "', n.aggregated=to_json(now()), n.aggregatorselector=to_json('" + aggregatorselector + "'::text), n.aggregatortake=to_json(" + str(aggregatortake) + "), n.aggregatortimefilter=to_json('" + aggregatortimefilter + "'::text), n.aggregatorskip=to_json(" + str(aggregatorskip) + "), n.aggregatorsort=to_json('" + aggregatorsort + "'::text), n.aggregatormethod=to_json('" + aggregatormethod + "'::text)")
            ncache.disconnect()
        if node['datasource']['type'] in ['L']:
            cproducers = dict()
            producers = s.iexpand(pattern=aggregatorselector, nodesdb=nodesdb, sort=aggregatorsort, take=aggregatortake, skip=aggregatorskip)
            ncache = Cache(nodesdb, objects=True)
            ncache.execute("match (n:nodes) where id(n) = '" + id+ "' set n.type=to_json('L'::text), n.icon=to_json('L'::text), n.producers='" + json.dumps(producers) + "', n.aggregated=to_json(now()), n.aggregatorselector=to_json('" + aggregatorselector + "'::text), n.aggregatortake=to_json(" + str(aggregatortake) + "), n.aggregatortimefilter=to_json('" + aggregatortimefilter + "'::text), n.aggregatorskip=to_json(" + str(aggregatorskip) + "), n.aggregatorsort=to_json('" + aggregatorsort + "'::text), n.aggregatormethod=to_json('" + aggregatormethod + "'::text)")
            ncache.disconnect()
            for p in producers:
                pchilds = s.igetnodes(nodesdb=nodesdb, parent=p['id'])
                for child in pchilds:
                    if child['datasource']['type'] in ['B','D']:
                        if child['name'] not in cproducers:
                            cproducers[child['name']] = [dict(id=child['id'], path=s.igetpath(id=child['id'], nodesdb=nodesdb))]
                        else:
                            cproducers[child['name']].append(dict(id=child['id'], path=s.igetpath(id=child['id'], nodesdb=nodesdb)))
                        
            nchilds = s.igetnodes(nodesdb=nodesdb, parent=node['id'])
            pnames = {x for x in cproducers.keys()}
            nnames = {x['name'] for x in nchilds}
            dids = {x['id'] for x in nchilds if x['name'] not in pnames}
            for e in dids:
                logging.info("Node: " + id + ", Type: " + node['datasource']['type'] + ", deleting obsolete child: '" + e + "' ...")
                s.ideletenode(id=e, nodesdb=nodesdb)
            for n in pnames - nnames:
                logging.info("Node: " + id + ", Type: " + node['datasource']['type'] + ", creating new child: '" + n + "' ...")
                s.icreatenode(id=node['id'], nodesdb=nodesdb, name=n)
            nchilds = s.igetnodes(nodesdb=nodesdb, parent=node['id'])
            for c in nchilds:
                if 'aggregatormethod' in c['datasource'] and 'aggregatortimefilter' in c['datasource']:
                    if c['datasource']['aggregatormethod'] != aggregatormethod or c['datasource']['aggregatortimefilter'] != aggregatortimefilter:
                        logging.info("Node: " + c['id']+ ", Type: " + c['datasource']['type'] + ", deleting cache if exists ...")
                        s.ideletecache(c['id'], nodesdb=nodesdb)
                tpath = [x['path'] for x in cproducers[c['name']]]
                aggregatorselector = '|'.join(tpath)
                ncache = Cache(nodesdb, objects=True)
                ncache.execute("match (n:nodes) where id(n) = '" + c['id'] + "' set n.type=to_json('A'::text), n.icon=to_json('A'::text), n.producers='" + json.dumps(cproducers[c['name']]) + "', n.aggregated=to_json(now()), n.aggregatorselector=to_json('" + aggregatorselector + "'::text), n.aggregatortake=to_json(" + str(aggregatortake) + "), n.aggregatortimefilter=to_json('" + aggregatortimefilter + "'::text), n.aggregatorskip=to_json(" + str(aggregatorskip) + "), n.aggregatorsort=to_json('" + aggregatorsort + "'::text), n.aggregatormethod=to_json('" + aggregatormethod + "'::text)")
                ncache.disconnect()
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True)[0]
        return web.json_response(dict(success=True, data=node))
     
    @intercept_logging_and_internal_error
    @trace_call
    def unload(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        logging.info("Unloading node: " + id + " ...")
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True)[0]
        path = s.igetpath(nodesdb=nodesdb, id=id)
        archive = path.replace('/', '_')[1:] + '-unload.zip'
        fname = '/ramdisk/' + archive
        zip = Arcfile(fname, 'w:zip')
        cut = 10000
        done = s.ibuildcollectioncache(node, collections={'*'}, systemdb=systemdb, nodesdb=nodesdb)
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True)[0]        
        hcache = Cache(node['datasource']['cache']['database'], schema=node['datasource']['cache']['name'])
        for collection in node['datasource']['collections']:
            logging.info("Unloading collection: " + collection + " ...")
            d = dict(collection=collection, desc=dict(), data=[])
            desc = OrderedDict()
            x = hcache.execute("select column_name, data_type from information_schema.columns where table_name = '" + collection.lower() + "' and table_schema = '" + node['datasource']['cache']['name'] + "'")
            for row in x.fetchall(): desc[row['column_name']] = row['data_type']

            #desc = hcache.desc(table=collection)
            request = 'select '
            for k in desc:
                if k != 'kairos_nodeid':
                    d['desc'][k] = desc[k]
                    request += k + ', '
            request = request[:-2] + ' from ' + collection
            recordset = 0
            nbrec = 0
            if len(desc) != 0:
                for x in hcache.execute(request):
                    nbrec += 1
                    r = dict()
                    for k in desc:
                        if k != 'kairos_nodeid': r[k] = x[k]
                    d['data'].append(r)
                    if nbrec == cut:
                        logging.info("Writing file: " + collection + str(recordset) + " ...")
                        zip.write(collection + str(recordset), json.dumps(d, sort_keys=True, indent=4))
                        recordset += 1
                        d['data']=[]
                        nbrec = 0
            if nbrec > 0: 
                logging.info("Writing file: " + collection + str(recordset) + " ...")
                zip.write(collection + str(recordset), json.dumps(d, sort_keys=True, indent=4))
        hcache.disconnect()
        zip.close()
        logging.info("Unloading node: " + id + ", file is ready to download !")
        return web.Response(headers=MultiDict({'Content-Disposition': 'Attachment;filename="' + archive + '"'}), body=open(fname, 'rb').read())
    
    @intercept_logging_and_internal_error
    @trace_call
    def linkfathernode(s, request):
        params = parse_qs(request.query_string)
        origindb = params['origindb'][0]
        targetdb = params['targetdb'][0]
        fromid = params['from'][0]
        toid = params['to'][0]
        fnode = s.igetnodes(nodesdb=origindb, id=fromid)[0]
        tnode = s.igetnodes(nodesdb=targetdb, id=toid)[0]
        fpath = s.igetpath(id=fromid, nodesdb=origindb)
        if fnode['status'] == 'DELETED' or tnode['status'] == 'DELETED':
            message = 'A trash cannot be part of a link operation!'
            return web.json_response(dict(success=False, status='error', message=message))
        producers = tnode['datasource']['producers']
        if fromid in producers:
            message = fpath + ': this node is already included in the list of producers!'
            return web.json_response(dict(success=False, status='error', message=message))   
        producers.append(dict(path=s.igetpath(nodesdb=origindb, id=fromid), id=fromid))
        ncache = Cache(targetdb, objects=True)
        if 'aggregatorselector' not in tnode['datasource']:
            ncache.execute("match (n:nodes) where id(n) = '" + toid + "' set n.type=to_json('L'::text), n.icon=to_json('L'::text), n.producers='" + json.dumps(producers) + "', n.aggregated=to_json(now()), n.aggregatorselector=to_json('" + s.igetpath(nodesdb=origindb, id=fromid) + "'::text), n.aggregatortake=to_json(1), n.aggregatortimefilter=to_json('.'::text), n.aggregatorskip=to_json(0), n.aggregatorsort=to_json('desc'::text), n.aggregatormethod=to_json('$none'::text)")
        else:
            ncache.execute("match (n:nodes) where id(n) = '" + toid + "' set n.type=to_json('L'::text), n.icon=to_json('L'::text), n.producers='" + json.dumps(producers) + "', n.aggregated=to_json(now()), n.aggregatorselector=to_json('" + tnode['datasource']['aggregatorselector'] + '|' + s.igetpath(nodesdb=origindb, id=fromid) + "'::text), n.aggregatortake=to_json(" + str(tnode['datasource']['aggregatortake'] +  1) + ")")
        ncache.disconnect()
        tnode = s.igetnodes(nodesdb=targetdb, id=toid, getsource=True)[0]
        return web.json_response(dict(success=True, data=tnode))

    @intercept_logging_and_internal_error
    @trace_call
    def applyliveobject(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        loname = params['liveobject'][0]
        id = params['id'][0]
        liveobject = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="{id:'" + loname + "', type:'liveobject'}")[0]
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        if node['datasource']['type'] in ['D']:
            logging.info("Node: " + id + ", Type: " + node['datasource']['type'] + ", deleting cache ...")
            s.ideletecache(id, nodesdb=nodesdb)
        s.icreatecache(id, nodesdb=nodesdb)
        cache = s.igetcache(id, nodesdb=nodesdb)
        (message, collections) = s.iapplyliveobject(id=id, cache=cache, liveobject=liveobject)
        ncache = Cache(nodesdb, objects=True)
        ncache.execute("match (n:nodes) where id(n) = '" + id+ "' set n.type=to_json('D'::text), n.icon=to_json('D'::text), n.aggregated=to_json(now()), n.liveobject=to_json('" + loname + "'::text)")
        ncache.disconnect()
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        if message: return web.json_response(dict(success=False, message=message))
        else: return web.json_response(dict(success=True, data=node))