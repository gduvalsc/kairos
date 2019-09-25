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
import string, random, ssl, logging, os, binascii, subprocess, zipfile, gzip, tarfile, bz2, shutil, re, json,  time, lxml.html, magic, cgi, sys, multiprocessing, pyinotify, urllib, base64, psycopg2, psycopg2.extras, psycopg2.extensions, queue, multiprocessing, multiprocessing.connection, io, time, plotly, pandas, hashlib
from pymemcache.client.base import Client
from collections import *
from datetime import datetime
from aiohttp import web, WSCloseCode, WSMsgType, MultiDict
from urllib.parse import parse_qs

logging.TRACE = 5
logging.addLevelName(5, "TRACE")
logging.trace = lambda m: logging.log(logging.TRACE, m)

global kairos
kairos=dict()

def getfontsize(width, binf=1000, bsup=2000, vinf=0, vsup=0):
    if width <= binf: return int(vinf)
    if width >= bsup: return int(vsup)
    return int(vinf + ((vsup - vinf) / (bsup - binf)) * (width - binf))

def getyposition(yaxis, width, numleftyaxis=1, binf=1000, bsup=2000, vinf=0.08, vsup=0.05, rows=1):
    begposition = yaxis['position']
    if begposition == 0: return begposition
    if begposition == 0.05 and numleftyaxis / rows == 1: return 0
    if begposition == 0.05:
        if width <= binf: return vinf
        if width >= bsup: return vsup
        return vinf + ((vsup -vinf) / (bsup - binf) * (width - binf))
    if begposition == 0.90:
        if width <= binf: return 1 - (2 * vinf)
        if width >= bsup: return 1 - (2 * vsup)
        return 1 - (2 * (vinf + ((vsup -vinf) / (bsup - binf) * (width - binf))))
    if begposition == 0.95:
        if width <= binf: return 1 - vinf
        if width >= bsup: return 1 - vsup
        return 1 - (1 * (vinf + ((vsup -vinf) / (bsup - binf) * (width - binf))))

def getaposition(width, index=0, numleftyaxis=1, numrightyaxis=0, numxaxis=1, binf=1000, bsup=2000, vinf=0.08, vsup=0.05, rows=1):
    if rows == 1:
        cols = numxaxis
        nbseparators = cols - 1
        lengthseparator = 0.02
        lengthseparators = lengthseparator * nbseparators
        lengthaxis = vinf if width <= binf else vsup if width >= bsup else vinf + ((vsup -vinf) / (bsup - binf) * (width - binf))
        lengthaxis = 0 if numleftyaxis + numrightyaxis == 0 else lengthaxis
        availablespace = 1 - ((numleftyaxis + numrightyaxis - 1) * lengthaxis) - 2 * lengthseparator
        lengthdomain = (availablespace - lengthseparators) / cols 
        positiondomain = (numleftyaxis - 1) * lengthaxis + lengthseparator + index * (lengthdomain + lengthseparator) 
        return positiondomain + lengthdomain / 2
    else:
        nbseparators = rows - 1
        lengthseparator = 0.02
        lengthseparators = lengthseparator * nbseparators
        availablespace = 1 - lengthseparators
        lengthdomain = (availablespace - lengthseparators) / rows
        positiondomain = lengthdomain + index * (lengthdomain + lengthseparator * 2)
        return positiondomain

def getdomain(width, index=0, numleftyaxis=1, numrightyaxis=0, numxaxis=1, binf=1000, bsup=2000, vinf=0.08, vsup=0.05, rows=1):
    cols = numxaxis if rows == 1 else 1
    nbseparators = cols - 1
    lengthseparator = 0.02
    lengthseparators = lengthseparator * nbseparators
    lengthaxis = vinf if width <= binf else vsup if width >= bsup else vinf + ((vsup -vinf) / (bsup - binf) * (width - binf))
    lengthaxis = 0 if numleftyaxis + numrightyaxis == 0 else lengthaxis
    availablespace = 1 - ((numleftyaxis / rows + numrightyaxis / rows  - 1) * lengthaxis) - 2 * lengthseparator
    lengthdomain = (availablespace - lengthseparators) / cols 
    positiondomain = (numleftyaxis / rows  - 1) * lengthaxis + lengthseparator + index * (lengthdomain + lengthseparator)
    return [positiondomain, positiondomain+lengthdomain]

def gettimestampdf(d, co, plotorientation):
    converttime = lambda x: datetime.strptime(x, '%Y%m%d%H%M%S%f')
    if  'timestamp' not in d[0] and plotorientation == 'horizontal':
        co['cols'] = len(d)
        co['isarray'] = True
    if  'timestamp' not in d[0] and plotorientation == 'vertical': 
        co['rows'] = len(d)
        co['isarray'] = True
    ret = []
    if co['isarray']:
        for x in d:
            r = pandas.DataFrame(data=x)
            r['timestamp'] = r['timestamp'].apply(converttime)
            r = r.set_index('timestamp').sort_index()
            ret.append(r)
    else:
        r = pandas.DataFrame(data=d)
        r['timestamp'] = r['timestamp'].apply(converttime)
        r = r.set_index('timestamp').sort_index()
        ret.append(r)
    return ret

def paddeddf(t, d):
    r = t.copy()
    r['a'] = 0
    r['b'] = d['value']
    r['value'] = r['a'] + r['b'].fillna(0)
    return r

def getnewaxis(co, reftimedf, template, axistype=None, options=None, index=0):
    if axistype == 'y' and index not in co['alreadyright']: co['alreadyright'][index] = False
    if axistype == 'y' and index not in co['alreadyleft']: co['alreadyleft'][index] = False
    d = co['yaxis'] if axistype == 'y' else co['xaxis']
    l = len(d)
    d[l] = dict()
    d[l]['name'] = axistype + 'axis' if l == 0 else  axistype + 'axis' + str(l + 1)
    d[l]['smallname'] = axistype if l == 0 else axistype + str(l + 1)
    if axistype == 'y':
        for e in template['yaxis']: d[l][e] = template['yaxis'][e].copy() if type(template['yaxis'][e]) == type(dict()) else template['yaxis'][e]
        d[l]['options']['title'] = options['title']
        if 'properties' in options and 'line' in options['properties'] and 'stroke' in options['properties']['line']: 
            d[l]['options']['tickfont'] = dict(color = options['properties']['line']['stroke'])
            d[l]['options']['color'] = options['properties']['line']['stroke']
            d[l]['options']['linecolor'] = options['properties']['line']['stroke']
        if 'properties' in options and 'text' in options['properties'] and 'fill' in options['properties']['text']: 
            d[l]['options']['titlefont'] = dict(color = options['properties']['text']['fill'])
        d[l]['options']['side'] = options['position'].lower()
        if d[l]['options']['side'] == 'left' and not co['alreadyleft'][index]: d[l]['options']['position'] = 0.05
        if d[l]['options']['side'] == 'left' and co['alreadyleft'][index]: 
            d[l]['options']['position'] = 0.00
            d[l]['options']['overlaying'] = 'y' if index == 0 else 'y' + str(index + 1)
        if d[l]['options']['side'] == 'right' and not co['alreadyright'][index]: 
            d[l]['options']['overlaying'] = 'y' if index == 0 else 'y' + str(index + 1)
            d[l]['options']['position'] = 0.95
        if d[l]['options']['side'] == 'right' and co['alreadyright'][index]: 
            d[l]['options']['overlaying'] = 'y' if index == 0 else 'y' + str(index + 1)
            d[l]['options']['position'] = 0.90
        if d[l]['options']['side'] == 'left': co['alreadyleft'][index] = True
        if d[l]['options']['side'] == 'right': co['alreadyright'][index] = True
        rows = co['rows']
        nbseparators = rows - 1
        lengthseparator = 0.02
        lengthseparators = lengthseparator * nbseparators
        lengthdomain = (1 - lengthseparators) / rows 
        positiondomain = 0.0 + index * (lengthdomain + lengthseparator)
        d[l]['options']['domain'] = [positiondomain, positiondomain + lengthdomain]
    else:
        for e in template['xaxis']: d[l][e] = template['xaxis'][e].copy() if type(template['xaxis'][e]) == type(dict()) else template['xaxis'][e]
        cols = co['cols']
        nbseparators = cols - 1
        lengthseparator = 0.02
        lengthseparators = lengthseparator * nbseparators
        lengthdomain = (0.8 - lengthseparators) / cols 
        positiondomain = 0.1 + index * (lengthdomain + lengthseparator)
        d[l]['options']['domain'] = [positiondomain, positiondomain + lengthdomain]
        d[l]['options']['range'] = [reftimedf[index].index.min(),reftimedf[index].index.max()]
    logging.debug('Axis index: ' + str(index) + ', options: ' + str(d[l]))
    return l

def settrace(co, r, dataframe=None, label=None, yaxisindex=0, index=0, alreadyinlegend = None, groupname=None, plotorientation=None, colors=None):
    getcolor = lambda x: colors[x] if x in colors else '#' + hashlib.md5(x.encode('utf-8')).hexdigest()[0:6]
    param = dict()
    param['x'] = dataframe.index
    param['y'] = dataframe['value']
    param['name'] = label
    param['legendgroup'] = label
    param['showlegend'] = True if label not in alreadyinlegend else False
    alreadyinlegend[label] = True
    if r['type'] == 'L': 
        param['line'] = dict(color=(getcolor(label)), shape='spline')
        trace = plotly.graph_objs.Scatter(**param)
    if r['type'] == 'A': 
        param['mode'] = 'lines'
        param['fill'] = 'tozeroy'
        param['fillcolor'] = getcolor(label)
        param['line'] = dict(color=(getcolor(label)), shape='spline')
        trace = plotly.graph_objs.Scatter(**param)
    if r['type'] == 'SA': 
        param['line'] = dict(color=(getcolor(label)), shape='spline')
        param['mode'] = 'lines'
        param['stackgroup'] = groupname
        param['fillcolor'] = getcolor(label)
        trace = plotly.graph_objs.Scatter(**param)
    if r['type'] == 'C': 
        param['marker']=dict(color=getcolor(label))
        trace = plotly.graph_objs.Bar(**param)
        co['layoutoptions']['barmode'] = 'group'
    if r['type'] == 'CC': 
        param['marker']=dict(color=getcolor(label))
        trace = plotly.graph_objs.Bar(**param)
        co['layoutoptions']['barmode'] = 'group'
    if r['type'] == 'SC': 
        param['marker']=dict(color=getcolor(label))
        trace = plotly.graph_objs.Bar(**param)
        co['layoutoptions']['barmode'] = 'stack'
    l = len(co['traces'])
    xaxis = index if co['shared_yaxes'] else 0
    yaxis = yaxisindex
    row = 1 if plotorientation=='horizontal' else index+1
    col = index+1 if plotorientation=='horizontal' else 1
    logging.debug('settrace, xaxis: ' + str(xaxis) + ', yaxis: ' + str(yaxis) + ', row: ' + str(row) + ', col:' + str(col) + ', label: ' + str(label))
    co['traces'][l] = dict(trace=trace, yaxis=yaxis, xaxis=xaxis, row=row, col=col)

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
        loglevel = logging.getLogger().getEffectiveLevel()
        if loglevel == logging.TRACE:
            tracef = open('/var/log/kairos/postgres_' + str(os.getpid()) + '.sql', 'a')
            print('-- >>> ' + func.__name__ + ' ' + str(datetime.now()), file=tracef)
            tracef.close()
        response = func(*args, **kwargs)
        if loglevel == logging.TRACE:
            tracef = open('/var/log/kairos/postgres_' + str(os.getpid()) + '.sql', 'a')
            print('-- <<< ' + func.__name__ + ' ' + str(datetime.now()), file=tracef)
            tracef.close()
        logging.debug('<<< Leaving %s ...' % func.__name__)
        return response
    return wrapper

def intercept_logging_and_internal_error(func):
    def wrapper(*args, **kwargs):
        request = args[1]
        params = parse_qs(request.query_string)
        if 'logging' in params:
            logger = logging.getLogger()
            if params['logging'][0] == 'trace': logger.setLevel(logging.TRACE)
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
            logging.error(str(tb))
            message = str(tb[1])
            return web.json_response(dict(success=False, message=message))
    return wrapper

def intercept_internal_error(func):
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            return response
        except:
            tb = sys.exc_info()
            logging.error(str(tb))
            message = str(tb[1])
            return web.json_response(dict(success=False, message=message))
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
class MemoryCache:
    def __init__(s, server, timeout=3600):
        s.memorycache = Client(server)
        s.timeout = timeout
    def get(s, key):
        memorykey = hashlib.md5(json.dumps(key).encode('utf-8')).hexdigest()
        jsonvalueout = s.memorycache.get(memorykey)
        if jsonvalueout:
            valueout = json.loads(jsonvalueout)
            now = int(datetime.now().strftime('%s'))
            timestamp = int(valueout['timestamp'])
            if now - timestamp > s.timeout: return None
            else: return valueout['value']
        else: return None 
    def set(s, key, valuein):
        memorykey = hashlib.md5(json.dumps(key).encode('utf-8')).hexdigest()
        listkey = hashlib.md5(json.dumps(key['id']).encode('utf-8')).hexdigest()
        jsonlistvalue = s.memorycache.get(listkey)
        listvalue = json.loads(jsonlistvalue) if jsonlistvalue else []
        if memorykey not in listvalue: 
            listvalue.append(memorykey)
            s.memorycache.set(listkey, json.dumps(listvalue))
        valueout = json.dumps(dict(timestamp=datetime.now().strftime('%s'), value=valuein))
        s.memorycache.set(memorykey, valueout)
    def flush(s, id):
        listkey = hashlib.md5(json.dumps(id).encode('utf-8')).hexdigest()
        jsonlistvalue = s.memorycache.get(listkey)
        listvalue = json.loads(jsonlistvalue) if jsonlistvalue else []
        for k in listvalue: s.memorycache.delete(k)

class Cache:
    def __init__(s,database=None, autocommit=False, objects=False, schema=None):
            postgresstr = "host='localhost' user='postgres' dbname='" + database + "'" if database != None else "host='localhost' user='postgres'"
            s.loglevel = logging.getLogger().getEffectiveLevel()
            s.tracefile = '/var/log/kairos/postgres_' + str(os.getpid()) + '.sql'
            s.trace('\n\n-- '+ str(datetime.now()))
            if database: s.trace('psql -d ' + database)
            else: s.trace('psql')
            s.trace('')
            s.postgres = psycopg2.connect(postgresstr)
            s.autocommit = autocommit
            s.schema = schema
            if autocommit: s.postgres.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            else: s.trace('BEGIN;')
            if schema: s.execute("set search_path = " + schema)
    def trace(s, stmt):
        if s.loglevel == logging.INFO:
            ftrace = open(s.tracefile, 'a')
            print(stmt, file=ftrace)
            ftrace.close()      
    def execute(s,*req):
        logging.debug('Executing request: ' + req[0])
        s.trace(req[0] + ';')
        c = s.postgres.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        c.execute(*req)
        logging.debug('Request completed!')
        return c     
    def executep(s,req,prm):
        logging.debug('Executing request: ' + req)
        c = s.postgres.cursor()
        c.execute(req, prm)
        logging.debug('Request completed!')
        return c
    def copy(s, buffer, table, description):
        logging.debug('Executing copy into: ' + table + " using: " + str(description))
        s.trace('COPY ' + table + " " + json.dumps(description).replace('[','(').replace(']',')') + ' FROM stdin;')
        s.trace(buffer.getvalue()[:-1])
        s.trace('\\.')
        c = s.postgres.cursor()
        c.copy_from(buffer, table, columns=description)
        logging.debug('Request completed!')
    def exists(s, table):
        result = False
        x = s.execute("select 1 from information_schema.tables where table_schema = '" + s.schema + "' and table_name = '" + table + "'")
        for rx in x.fetchall(): result = True
        return result
    def commit(s):
        if not s.autocommit:
            s.trace('COMMIT;') 
            s.postgres.commit()
    def rollback(s):
        if not s.autocommit:
            s.trace('ROLLBACK;') 
            s.postgres.rollback()
    def disconnect(s):
        if not s.autocommit: 
            s.trace('COMMIT;') 
            s.postgres.commit()
        s.trace('\\q')
        s.postgres.close()

class Arcfile:
    def __init__(s,file,mode='r'):
        s.lock = multiprocessing.Lock()
        opmode=mode.split(':')
        s.type='unknown'
        if opmode[0] in ['r','a']:
            if zipfile.is_zipfile(file):
                s.archive=zipfile.ZipFile(file,mode)
                s.type='zipfile'
            else:
                file.seek(0)
                try:
                    s.archive=tarfile.open(fileobj=file)
                    s.type='tarfile'
                except:
                    logging.error('Unknown file type')
        else:
            if len(opmode)>1 and opmode[1] in ['zip']:
                s.type='zipfile'
                s.archive=zipfile.ZipFile(file,opmode[0],zipfile.ZIP_DEFLATED)
            else: s.archive=tarfile.open(name='stream', mode='w+b', fileobj=file)
    def close(s):
        return s.archive.close()
    def list(s):
        if s.type=='tarfile': return s.archive.getnames()
        else: return s.archive.namelist()
    def read(s,member):
        s.lock.acquire()
        if s.type=='tarfile':
            try: 
                r = bz2.decompress(s.archive.extractfile(s.archive.getmember(member).name).read())
            except: 
                r = s.archive.extractfile(s.archive.getmember(member).name).read()
        else:
            try: 
                r = bz2.decompress(s.archive.read(member))
            except: 
                r = s.archive.read(member)
        s.lock.release()
        return r
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
                status = os.system('kairos -s uploadnode --systemdb kairos_system_system --nodesdb ' + os.path.basename(event.path) + ' --file ' + event.pathname)
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
        app.router.add_get('/export', s.exportdatabase)
        app.router.add_get('/import', s.importdatabase)
        app.router.add_get('/cleardependentcaches', s.cleardependentcaches)
        app.router.add_get('/builddependentcaches', s.builddependentcaches)
        app.router.add_get('/clearmemorycaches', s.clearmemorycaches)
        app.router.add_get('/runchart', s.runchart)
        app.router.add_post('/changepassword', s.changepassword)
        app.router.add_post('/uploadobject', s.uploadobject)
        app.router.add_post('/setobject', s.setobject)
        app.router.add_post('/checkuserpassword', s.checkuserpassword)
        app.router.add_post('/uploadnode', s.uploadnode)
        app.router.add_static('/resources/', path='/kairosx/resources', name='resources')
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
        return web.Response(content_type='text/html', text=open('/kairosx/index.html').read())

    def file_charter(s, request):
        return web.Response(content_type='application/octet-stream', text=open('/kairosx/charter.js').read())

    def file_client(s, request):
        return web.Response(content_type='application/octet-stream', text=open('/kairosx/client.js').read())
        
    @trace_call
    def ideletecache(s, nid, nodesdb=None, context=None):
        status = Object()
        status.error = None
        logging.info("Node: " + str(nid) + ", dropping all caches ...")
        try:
            ncache = Cache(nodesdb, autocommit=True) if not context else context
            ncache.execute("delete from caches where id = " + str(nid))
            try: ncache.execute("drop schema cache_" + str(nid) + " cascade")
            except: pass
            if not context: ncache.disconnect()
            memorycache = MemoryCache(('localhost', 11211))
            memorycache.flush(nid)
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status
        
    @trace_call
    def ideletesource(s, nid, nodesdb=None, context=None):
        ncache = Cache(nodesdb, autocommit=True) if not context else context
        ncache.execute("delete from sources where id=" + str(nid))
        if not context: ncache.disconnect()

    @trace_call
    def icreatecache(s, nid, nodesdb=None, context=None):
        ncache = Cache(nodesdb, autocommit=True) if not context else context
        schname = 'cache_' + str(nid)
        ncache.execute("create schema " + schname)
        ncache.execute("insert into caches (id, name, created, queries, collections) values(%s, %s, now(), %s, %s)", (nid, schname, json.dumps(dict()), json.dumps(dict())))
        if not context: ncache.disconnect()
        
    @trace_call
    def icreatesource(s, nid, nodesdb=None, systemdb=None, stream=None, filename=None, context=None):
        filepath = '/tmp/' + nodesdb + '_' + str(nid) + '.zip'
        infile = Arcfile(stream, 'r')
        ziparchive = Arcfile(filepath, 'w:zip')
        for m in infile.list(): ziparchive.write(m, infile.read(m))
        ziparchive.close()
        collections = dict()
        def listener(col, d, v, n):
            for x in v['collections']:
                if x not in collections: collections[x] = dict(analyzer=v['analyzer'],members=[])
                collections[x]['members'].append(v['member'])
        analmain = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='ANALMAIN' and type='analyzer'")[0]
        analyzer = Analyzer(analmain, {}, listener, None)
        def do(member):
            logging.info('Analyzing member: ' + member + '...')
            analyzer.analyze(ziparchive.read(member), member)
            return None
        logging.info('Analyzing archive: ' + filepath + '...')
        ziparchive = Arcfile(filepath, 'r')
        for member in ziparchive.list(): do(member)
        ziparchive.close()
        ncache = Cache(nodesdb, autocommit=True) if not context else context
        f=open(filepath, 'rb')
        content = binascii.b2a_base64(f.read())
        f.close()
        os.unlink(filepath)
        ncache.executep("insert into sources (id, created, collections, stream) values(%s, now(), %s, %s)", (nid, json.dumps(collections), content))
        ncache.execute("update nodes set type = 'B', icon='B' where id = " + str(nid))
        if not context: ncache.disconnect()
        
    @trace_call
    def igetcache(s, nid, nodesdb=None, context=None):
        ncache = Cache(nodesdb, autocommit=True) if not context else context
        x = ncache.execute("select id as rid, name, queries, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created, collections from caches where id = " + str(nid))
        r = Object()
        for rx in x.fetchall():
            r.rid = rx['rid']
            r.name = rx['name']
            r.queries = json.loads(rx['queries'])
            r.created = rx['created']
            r.collections = json.loads(rx['collections'])
        if not context: ncache.disconnect()
        return r
        
    @trace_call
    def igetsource(s, nid, nodesdb=None, context=None, stream=False):
        ncache = Cache(nodesdb, autocommit=True) if not context else context
        if stream: x = ncache.execute("select id as rid, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created, collections, stream from sources where id = " + str(nid))
        else: x = ncache.execute("select id as rid, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created, collections from sources where id = " + str(nid))
        r = Object()
        for rx in x.fetchall():
            r.rid = rx['rid']
            r.created = rx['created']
            r.collections = json.loads(rx['collections'])
            if stream: r.stream = binascii.a2b_base64(rx['stream'])
        if not context: ncache.disconnect()
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
        ncache = Cache('kairos_system_system', autocommit=True)        
        ncache.execute("create extension plpythonu")
        ncache.execute("create sequence objid start 1")
        ncache.execute("create table objects(rid integer primary key, id text, type name, created timestamp, filename text, stream bytea)")        
        ncache.execute("create unique index iobjects on objects(id, type)")        
        ncache.disconnect()
        logging.info("kairos_system_system database created.")

    @trace_call
    def icreaterole(s, role=None):
        curdatabase = "kairos_group_" + role
        ncache = Cache(None, autocommit=True)        
        x = ncache.execute("select datname from pg_database")
        databases = [row['datname'] for row in x.fetchall()]
        if curdatabase in databases: 
            ncache.disconnect()
            return dict(success=False, message=role + ' role already exists!')
        logging.info("Creating a new " + curdatabase + " database ...")
        ncache.execute("create database kairos_group_" + role + " with encoding 'utf8'")
        logging.info(curdatabase + " database created.")
        ncache.execute("create role " + role)
        logging.info(role + " role created.")
        ncache.disconnect()
        ncache = Cache("kairos_group_" + role)        
        ncache.execute("create language plpythonu")
        ncache.execute("create extension oracle_fdw")
        ncache.execute("create extension postgres_fdw")
        ncache.execute("create sequence objid start 1")
        ncache.execute("create table objects(rid integer primary key, id text, type name, created timestamp, filename text, stream bytea)")
        ncache.execute("create unique index iobjects on objects(id, type)")        
        ncache.execute("create table nodes(id integer primary key, parent integer references nodes(id), name text, type text, created timestamp, status text, icon text, liveobject text, aggregatorselector text, aggregatorsort text, aggregatortake integer, aggregatorskip integer, aggregatormethod text, aggregatortimefilter text, aggregated timestamp, producers text)")
        ncache.execute("create table sources(id integer primary key, created timestamp, collections text, stream bytea)")
        ncache.execute("create table caches(id integer primary key, name text, created timestamp, queries text, collections text)")
        for row in ncache.execute("select nextval('objid') as objid"): objid = row['objid']
        ncache.execute("insert into nodes(id, parent, name, type, created, status, icon) values (" + str(objid) + ", null, '/', 'N', now(), 'ACTIVE', 'N')")
        ncache.execute("insert into nodes(id, parent, name, type, created, status, icon) values (nextval('objid'), " + str(objid) + ", 'Trash', 'T', now(), 'DELETED', 'T')")
        ncache.disconnect()
        try: shutil.rmtree('/autoupload/' + curdatabase)
        except: pass
        os.mkdir('/autoupload/' + curdatabase)
        logging.info(curdatabase + " database created.")
        return dict(success=True, data=dict(msg=role + " role has been successfully created!"))

    @trace_call
    def icreateuser(s, user=None):
        curdatabase = "kairos_user_" + user
        ncache = Cache(None, autocommit=True)
        x = ncache.execute("select datname from pg_database")
        databases = [row['datname'] for row in x.fetchall()]
        if curdatabase in databases:
            ncache.disconnect()
            return dict(success=False, message=user + ' user already exists!')
        logging.info("Creating a new " + curdatabase + " database ...")
        ncache.execute("create database kairos_user_" + user + " with encoding 'utf8'")
        logging.info(curdatabase + " database created.")
        ncache.execute("create user " + user + " password '" + user + "'")
        logging.info(user + " user created.")
        ncache.disconnect()
        ncache = Cache("kairos_user_" + user, autocommit=True)
        ncache.execute("create language plpythonu")
        ncache.execute("create extension oracle_fdw")
        ncache.execute("create extension postgres_fdw")
        ncache.execute("create sequence objid start 1")
        ncache.execute("create table objects(rid integer primary key, id text, type name, created timestamp, filename text, stream bytea)")
        ncache.execute("create unique index iobjects on objects(id, type)")        
        ncache.execute("create table nodes(id integer primary key, parent integer references nodes(id), name text, type text, created timestamp, status text, icon text, liveobject text, aggregatorselector text, aggregatorsort text, aggregatortake integer, aggregatorskip integer, aggregatormethod text, aggregatortimefilter text, aggregated timestamp, producers text)")
        ncache.execute("create table settings(colors text, logging text, nodesdb text, plotorientation text, systemdb text, template text, top integer, wallpaper text)")
        ncache.execute("create table sources(id integer primary key, created timestamp, collections text, stream bytea)")
        ncache.execute("create table caches(id integer primary key, name text, created timestamp, queries text, collections text)")
        ncache.execute("insert into settings(colors, logging, nodesdb, plotorientation, systemdb, template, top, wallpaper) values ('COLORS', 'info', 'kairos_user_" + user + "', 'horizontal', 'kairos_system_system', 'DEFAULT', 15, 'DEFAULT')")
        for row in ncache.execute("select nextval('objid') as objid"): objid = row['objid']
        ncache.execute("insert into nodes(id, parent, name, type, created, status, icon) values (" + str(objid) + ", null, '/', 'N', now(), 'ACTIVE', 'N')")
        ncache.execute("insert into nodes(id, parent, name, type, created, status, icon) values (nextval('objid'), " + str(objid) + ", 'Trash', 'T', now(), 'DELETED', 'T')")
        ncache.disconnect()        
        try: shutil.rmtree('/autoupload/' + curdatabase)
        except: pass
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
        logging.info(dbgroup + " database removed.")
        return dict(success=True, data=dict(msg=role + " role has been successfully removed!"))

    @trace_call
    def ideleteuser(s, user=None, admin=False):
        if user=='admin' and not admin: return dict(success=False, message='admin user cannot be removed!')
        dbuser = "kairos_user_" + user
        logging.info("Dropping " + dbuser + " database...")
        ncache = Cache(None, autocommit=True)
        ncache.execute("drop database " + dbuser)
        ncache.execute("drop user " + user)
        ncache.disconnect()
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
            ncache = Cache(db, autocommit=True)
            y = ncache.execute("select rid, id, type, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created from objects " + where)
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
            ncache = Cache(db)
            x = ncache.execute("select filename, stream as content, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created from objects " + where)
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
    def iexecutequery(s, nodesdb=None, systemdb=None, id=None, query=None, limit=None, variables=None):
        global kairos
        for v in variables: kairos[v] = variables[v]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True, getstream=True)[0]
        query = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + query + "' and type='query'")[0]
        status = s.ibuildcollectioncache(node, collections=query['collections'], systemdb=systemdb, nodesdb=nodesdb)
        if status.error: return status
        status = s.ibuildquerycache(node, query=query, systemdb=systemdb, nodesdb=nodesdb)
        if status.error: return status
        status = s.iqueryexecute(node, query=query, nodesdb=nodesdb, limit=limit)
        return status

    @trace_call
    def igetnodes(s, nodesdb=None, id=None, name=None, parent=None, root=False, child=None, countchildren=False, getsource=False, getcache=False, getstream=False):
        ncache = Cache(nodesdb)
        projection1 = "id as rid, type, name, icon, status, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created, liveobject, aggregatorselector, aggregatorsort, aggregatortake, aggregatorskip, aggregatormethod, aggregatortimefilter, to_char(aggregated, 'YYYY-MM-DD HH24:MI:SS.MS') as aggregated, producers"
        projection2 = "parent as rid, type, name, icon, status, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created, liveobject, aggregatorselector, aggregatorsort, aggregatortake, aggregatorskip, aggregatormethod, aggregatortimefilter, to_char(aggregated, 'YYYY-MM-DD HH24:MI:SS.MS') as aggregated, producers"
        if root: x = ncache.execute("select " + projection1 + " from nodes where name = '/'")
        if name and parent: x = ncache.execute("select " + projection1 + " from nodes where parent = " + str(parent) + " and name ='" + name + "'")
        if not name and parent: x = ncache.execute("select "+ projection1 + " from nodes where parent = " + str(parent))
        if not name and child: x = ncache.execute("select " + projection2 + " from nodes where id = " + str(child))
        if id: x = ncache.execute("select " + projection1 + " from nodes where id = " + str(id))
        selectednodes = [row for row in x.fetchall()]
        ncache.disconnect()
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
                    liveobject = s.igetobjects(nodesdb=nodesdb, systemdb='kairos_system_system', where="where id='" + row['liveobject'] + "' and type='liveobject'")[0]
                    for e in liveobject['tables']: d[e] = True
                except: pass
                node['datasource']['collections'] = d
            if countchildren:
                ncache = Cache(nodesdb)
                x = ncache.execute("select count(*) as count from nodes where parent = " + str(node['id']))
                for r in x.fetchall(): node['kids'] = r['count']
                ncache.disconnect()
            if getsource:
                if row['type'] == 'B':
                    source = s.igetsource(node['id'], nodesdb=nodesdb, stream=getstream)
                    if hasattr(source, 'rid'):
                        node['datasource']['uploaded'] = source.created
                        node['datasource']['collections'] = source.collections
                        if getstream: node['datasource']['stream'] = source.stream
                if row['type'] in ['A', 'C']:
                    try:
                        firstproducer = s.igetnodes(nodesdb=nodesdb, id=node['datasource']['producers'][0]['id'], getsource=True)[0]
                        node['datasource']['collections'] = firstproducer['datasource']['collections']
                    except: node['datasource']['collections'] = None
            if getcache:
                if row['type'] in ['A', 'B', 'D', 'C']:
                    cache = s.igetcache(node['id'], nodesdb=nodesdb)
                    if hasattr(cache, 'rid'):
                        node['datasource']['cache']['collections'] = cache.collections
                        node['datasource']['cache']['queries'] = cache.queries
                        node['datasource']['cache']['name'] = cache.name
            nodes.append(node)
        return nodes
    
    @trace_call
    def igetpath(s, nodesdb=None, id=None):
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        return '' if node['name'] == '/' else s.igetpath(nodesdb=nodesdb, id=s.igetnodes(nodesdb=nodesdb, child=id)[0]['id']) + '/' + node['name']

    @trace_call
    def icreatenode(s, nodesdb=None, id=None, name=None, context=None):
        ncache = Cache(nodesdb, autocommit=True) if not context else context
        if not name:
            x = ncache.execute("select to_char(now(), 'YYYY-MM-DD HH24:MI:SS.MS') as name")
            for row in x.fetchall(): name = row['name']
        for row in ncache.execute("select nextval('objid') as objid"): objid = row['objid']
        ncache.execute("insert into nodes(id, parent, name, type, created, status, icon) values (" + str(objid) + ", " + str(id) + ", '" + name + "', 'N', now(), 'ACTIVE', 'N')")
        if not context: ncache.disconnect()              
        return objid

    @trace_call
    def ideletenode(s, nodesdb=None, id=None):
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True)[0]
        root = s.igetnodes(nodesdb=nodesdb, root=True)[0]
        trash = s.igetnodes(nodesdb=nodesdb, parent=root['id'], name='Trash')[0]
        if root['id'] == node['id']: return 'Root node cannot be removed!'
        if node['datasource']['type'] == 'T': return 'A trash cannot be removed!'
        ncache = Cache(nodesdb, autocommit=True)
        if node['status'] == 'DELETED':
            x = ncache.execute("with recursive tree as (select id, parent from nodes where id = " + str(id) + " union all select p.id, p.parent from nodes p join tree c on p.parent = c.id) select id as rid from tree")
            listnodes = [row['rid'] for row in x.fetchall()]
            for rid in listnodes:
                s.ideletesource(rid, nodesdb=nodesdb, context=ncache)
                s.ideletecache(rid, nodesdb=nodesdb, context=ncache)
            ncache.execute("with recursive tree as (select id, parent from nodes where id = " + str(id) + " union all select p.id, p.parent from nodes p join tree c on p.parent = c.id) delete from nodes where id in (select id from tree)")
        else:
            ncache.execute("update nodes set parent = " + str(trash['id']) + " where id = " + str(id))
            ncache.execute("with recursive tree as (select id, parent from nodes where id = " + str(id) + " union all select p.id, p.parent from nodes p join tree c on p.parent = c.id) update nodes set status = 'DELETED' where id in (select id from tree)")
        ncache.disconnect()              
        return None
    
    @trace_call
    def iapplyliveobject(s, id=None, cache=None, liveobject=None, nodesdb=None):
        hcache = Cache(nodesdb, schema=cache.name)
        extension = liveobject['extension']
        server = liveobject['id']
        options = liveobject['options']
        hcache.execute('drop server if exists ' + server + ' cascade')
        hcache.execute('create server ' + server + ' foreign data wrapper ' + extension + " options (" + options + ")")
        hcache.execute('grant usage on foreign server ' + server + ' to postgres')
        user = liveobject['user']
        password = liveobject['password']
        hcache.execute('create user mapping for postgres server ' + server + " options (user '" + user + "', password '" + password + "')")
        collections = []
        message = None
        for t in liveobject['tables']:
            description = liveobject['tables'][t]['description']
            if extension == 'oracle_fdw': request = liveobject['tables'][t]['request']
            if extension == 'postgres_fdw': schema = liveobject['tables'][t]['schema']
            if extension == 'oracle_fdw': logging.debug('Foreign request: ' + request)
            if extension == 'postgres_fdw': logging.debug('Foreign table: ' + t)
            desc = ", ".join(["%(k)s %(v)s" % dict(k=d, v=description[d]) for d in description])
            if extension == 'oracle_fdw': hcache.execute('create foreign table foreign_' + t + '(' + desc + ') server ' + server + " options (table '(" + request.replace("'", "''").replace('kairos_nodeid_to_be_replaced', str(id)) + ")')")
            if extension == 'postgres_fdw': hcache.execute('create foreign table foreign_' + t + '(' + desc + ') server ' + server + " options (schema_name '" + schema + "', table_name '" + t + "')")
            collections.append(t)
        hcache.disconnect()
        return (message, collections)

    @trace_call
    def icheckcolcachetypeA(s, node, cache=None, collections=None, nodesdb=None, systemdb=None):
        nid = node['id']
        ntype = node['datasource']['type']
        status = Object()
        status.error = None
        status.todo = dict()
        status.mapproducers = dict()
        datepart = dict()
        try:
            for collection in collections:
                status.mapproducers[collection] = dict(deleted=dict(), created=dict(), updated=dict(), unchanged=dict())
                datepart[collection] = dict()
                for part in cache.collections[collection]: status.mapproducers[collection]['deleted'][part] = dict(id=part)
            node = s.igetnodes(nodesdb=nodesdb, id=nid, getcache=True)[0]
            producers = s.iexpand(pattern=node['datasource']['aggregatorselector'], nodesdb=nodesdb, sort=node['datasource']['aggregatorsort'], skip=node['datasource']['aggregatorskip'], take=node['datasource']['aggregatortake'])
            ncache = Cache(nodesdb, autocommit=True)
            ncache.execute("update nodes set producers='" + json.dumps(producers) + "', aggregated=now() where id = " + str(nid))
            ncache.disconnect()              
            for producer in node['datasource']['producers']:
                pid = str(producer['id'])
                for collection in collections:        
                    datepart[collection][pid] = cache.collections[collection][pid] if pid in cache.collections[collection] else None
                    if pid in status.mapproducers[collection]['deleted']:
                        del status.mapproducers[collection]['deleted'][pid]
                        status.mapproducers[collection]['unchanged'][pid] = producer
                    else: status.mapproducers[collection]['created'][pid] = producer
                    if datepart[collection][pid] == None and pid in status.mapproducers[collection]['unchanged']:
                        del status.mapproducers[collection]['unchanged'][pid]
                        status.mapproducers[collection]['updated'][pid] = producer
                pnode = s.igetnodes(nodesdb=nodesdb, id=producer['id'], getsource=True, getcache=True, getstream=True)[0]
                bstatus = s.ibuildcollectioncache(pnode, collections=collections, systemdb=systemdb, nodesdb=nodesdb)
                pdone = bstatus.todo
                pcache = s.igetcache(pnode['id'], nodesdb=nodesdb)
                ptype = pnode['datasource']['type']
                for collection in collections:
                    if pdone[collection] and pid in status.mapproducers[collection]['unchanged']:
                        del status.mapproducers[collection]['unchanged'][pid]
                        status.mapproducers[collection]['updated'][pid] = producer
                    for p in pcache.collections[collection]:
                        if datepart[collection][pid] != None and pcache.collections[collection][p] > datepart[collection][pid] and pid in status.mapproducers[collection]['unchanged']:
                            del status.mapproducers[collection]['unchanged'][pid]
                            status.mapproducers[collection]['updated'][pid] = producer
                    #if ptype in 'D': status.mapproducers[collection]['updated'][pid] = producer
                    status.todo[collection] = True if len(status.mapproducers[collection]['deleted']) + len(status.mapproducers[collection]['created']) + len(status.mapproducers[collection]['updated']) > 0 else False
            for collection in collections:
                message = "Node: " + str(nid) + ", Type: " + ntype + ", Collection: '" + collection + "'"
                message += ", Producers: (Unchanged: "
                for x in status.mapproducers[collection]['unchanged']: message += str(x) + ','
                message += " Updated: "
                for x in status.mapproducers[collection]['updated']: message += str(x) + ','
                message += " New: "
                for x in status.mapproducers[collection]['created']: message += str(x) + ','
                message += " Deleted: "
                for x in status.mapproducers[collection]['deleted']: message += str(x) + ','
                message += ")"
                logging.info(message)
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status

    @trace_call
    def icheckcolcachetypeB(s, node, cache=None, collections=None, nodesdb=None, systemdb=None):
        status = Object()
        status.error = None
        status.todo = dict()
        status.analyzers = dict ()
        try:
            nid = node['id']
            ntype = node['datasource']['type']
            for collection in collections:
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", checking collection cache: '" + collection + "' ...")
                status.todo[collection] = False
                analyzername = node ['datasource']['collections'][collection]['analyzer']
                analyzer = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id ='" + analyzername + "' and type = 'analyzer'")[0]
                datepart = cache.collections[collection][str(nid)] if collection in cache.collections and str(nid) in cache.collections[collection] else None
                status.todo[collection] = True if datepart == None else status.todo[collection]
                status.todo[collection] = True if datepart != None and node['datasource']['uploaded'] > datepart else status.todo[collection]
                status.todo[collection] = True if datepart != None and analyzer['created'] > datepart else status.todo[collection]
                status.analyzers[collection] = analyzer
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status

    @trace_call
    def icheckcolcachetypeD(s, node, cache=None, collections=None, nodesdb=None, systemdb=None):
        status = Object()
        status.error = None
        status.todo = dict()
        try:
            nid = node['id']
            ntype = node['datasource']['type']
            liveobject = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + node['datasource']['liveobject'] + "' and type='liveobject'")[0]
            try: timeout = liveobject['retention']
            except: timeout = 60
            for collection in collections:
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", checking collection cache: '" + collection + "' ...")
                status.todo[collection] = False
                datepart = cache.collections[collection][str(nid)] if str(nid) in cache.collections[collection] else None
                status.todo[collection] = True if datepart == None else status.todo[collection]
                status.todo[collection] = True if datepart != None and (datetime.now() - datetime.strptime(datepart, '%Y-%m-%d %H:%M:%S.%f')).seconds > timeout else status.todo[collection]                   
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status

    @trace_call
    def idropcolcachetypeA(s, node, cache=None, collection=None, mapproducers=None, nodesdb=None):
        status = Object()
        status.error = None
        try:
            exclude = [str(x) for x in mapproducers[collection]['unchanged'].keys()]
            hcache = Cache(nodesdb, schema=cache.name)
            if len(exclude) == 0: hcache.execute("drop table if exists " + collection)
            if len(exclude) == 1: 
                if hcache.exists(collection): hcache.execute("delete from " + collection + " where kairos_nodeid not in ('" + exclude[0] + "')")
            if len(exclude) > 1: 
                if hcache.exists(collection): hcache.execute("delete from " + collection + " where kairos_nodeid not in " + str(tuple(exclude)))
            hcache.disconnect()
            for x in mapproducers[collection]['deleted'] : del cache.collections[collection][x]
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status

    @trace_call
    def idropcolcachetypeB(s, node, cache=None, collection=None, nodesdb=None):
        status = Object()
        status.error = None
        try:
            hcache = Cache(nodesdb, schema=cache.name)
            hcache.execute("drop table if exists " + collection)
            hcache.disconnect()
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status

    @trace_call
    def idropcolcachetypeD(s, node, cache=None, collection=None, nodesdb=None):
        status = Object()
        status.error = None
        try:
            hcache = Cache(nodesdb, schema=cache.name)
            hcache.execute("drop table if exists " + collection)
            hcache.disconnect()
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status

    @trace_call
    def idropcollectioncache(s, node, collection=None, nodesdb=None):
        status = Object()
        status.error = None
        try:
            nid = node['id']
            logging.info("Node: " + str(nid) + ", dropping collection cache: '" + collection + "' ...")
            cache = s.igetcache(nid, nodesdb=nodesdb)
            if hasattr(cache, 'name'):
                hcache = Cache(nodesdb, schema=cache.name, autocommit=True)
                hcache.execute("drop table if exists " + collection)
                hcache.disconnect()
            if hasattr(cache, 'collections'):
                if collection in cache.collections: del cache.collections[collection]
                ncache = Cache(nodesdb, autocommit=True)
                ncache.execute("update caches set collections = '" + json.dumps(cache.collections) + "' where id = " + str(nid))
                ncache.disconnect()
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status

    @trace_call
    def ibuildcolcachetypeA(s, node, cache=None, collection=None, mapproducers=None, nodesdb=None, systemdb=None):
        status = Object()
        status.error = None
        try:
            nid = node['id']
            ntype = node['datasource']['type']
            logging.info("Node: " + str(nid) + ", Type: " + ntype + ", building new collection cache: '" + collection + "' ...")
            hcache = Cache(nodesdb, schema=cache.name)
            function = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + node['datasource']['aggregatormethod'] + "' and type='aggregator'")[0]
            meet = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='meet' and type='function'")[0]
            hcache.execute(function["function"])
            hcache.execute(meet["function"])
            hcache.execute("drop table if exists aggregator")
            hcache.execute("create table aggregator as select '" + node['datasource']['aggregatormethod'] + "'::text as method")
            producers = list(mapproducers[collection]['updated'].keys())
            producers.extend(list(mapproducers[collection]['created'].keys()))
            x = hcache.execute("select distinct table_name from information_schema.columns where table_schema='" + cache.name + "'")
            schdesc = [row['table_name'] for row in x.fetchall()]
            for producer in producers:
                pnode = s.igetnodes(nodesdb=nodesdb, id=producer, getcache=True)[0]
                inschname = pnode['datasource']['cache']['name']
                x = hcache.execute("select distinct table_name from information_schema.columns where table_schema='" + inschname + "'")
                inschdesc = [row['table_name'] for row in x.fetchall()]
                if collection.lower() not in inschdesc: continue
                if collection.lower() not in schdesc: 
                    hcache.execute("create table " + collection.lower() + " as select * from " + inschname + "." + collection.lower() + " limit 0")
                    break
            # At this point the new collection is created but empty

            tabledesc = OrderedDict()
            x = hcache.execute("select column_name, data_type from information_schema.columns where table_name = '" + collection.lower() + "' and table_schema = '" + cache.name + "'")
            for row in x.fetchall(): tabledesc[row['column_name']] = row['data_type']
            hcache.disconnect()
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message

        
        queue = multiprocessing.Queue()
        error_queue = multiprocessing.Queue()

        def write_to_queue(producer):
            try:
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", building partition for producer: '" + str(producer) + "' ...")
                pnode = s.igetnodes(nodesdb=nodesdb, id=producer, getcache=True)[0]
                inschname = pnode['datasource']['cache']['name']
                lgby = [k for k in tabledesc if tabledesc[k] == 'text']
                lavg = [k for k in tabledesc if tabledesc[k] == 'real']
                lsum = [k for k in tabledesc if tabledesc[k] in ['integer', 'bigint']]
                listf = tabledesc.keys()
                where = " where meet(timestamp,'" + node['datasource']['aggregatortimefilter'] + "') or timestamp='00000000000000000'" if 'timestamp' in lgby else ' '
                subrequest = "select * from " + inschname + "." + collection.lower() + where
                request = "select "
                for x in lgby: request = request + function["name"] + '(timestamp) as timestamp, ' if x == "timestamp" else request + x + ', '
                for x in lavg: request += 'sum(coalesce(' + x + ', 0)) as ' + x + ', '
                for x in lsum: request += 'sum(' + x + ') as ' + x + ', '
                request = request[:-2] + ' from (' + subrequest + ') as foo group by '
                for x in lgby: request = request + function["name"] + '(timestamp), ' if x == 'timestamp' else request + x + ', '
                request = request[:-2]
                workrequest = 'select ' + function["name"] + '(timestamp) as timestamp, kairos_nodeid, count(*) num from (select distinct timestamp, kairos_nodeid from ' + inschname  + '.' + collection + where +') as foo group by ' + function["name"] + '(timestamp), kairos_nodeid'
                divisor = dict()
                hcache = Cache(nodesdb, schema=cache.name)
                if 'timestamp' in lgby:  
                    for x in hcache.execute(workrequest).fetchall(): divisor[x['timestamp'] + x ['kairos_nodeid']] = x['num']
                if len(lgby) > 0:
                    for row in hcache.execute(request).fetchall():
                        record = ''
                        if 'timestamp' in lgby:
                            for x in lavg: row[x] = row[x] * 1.0 / divisor[row['timestamp'] + row['kairos_nodeid']]
                        for k in tabledesc.keys(): record += '\\N\t' if row[k] == None else str(row[k]).replace('\n','\\n').replace('\t','\\t').replace('\r', '').replace('\\', '\\\\') + '\t'
                        record = record[:-1] + '\n'
                        queue.put(record)
                hcache.disconnect()
            except:
                tb = sys.exc_info()
                message = str(tb[1])
                logging.error(message)
                error_queue.put(producer)

        def read_from_queue(col):
            hcache = Cache(nodesdb, schema=cache.name)
            buffer = io.StringIO()
            bufferempty = True
            counter = 0
            try: limit = int(os.environ['BUFFER'])
            except: limit = 10000
            globalcounter = 0
            while True:
                try:
                    record = queue.get()
                    if record == 'KAIROS_DONE': break
                    bufferempty = False
                    counter += 1
                    logging.debug('Buffer content at line: ' + str(counter) + ', record: ' + str(record))
                    buffer.write(record)
                    if counter == limit:
                        buffer.seek(0)
                        logging.info("Writing " + str(counter) + " records to collection: " + col + "...")
                        hcache.copy(buffer, col, tuple(tabledesc.keys()))
                        #hcache.commit()
                        buffer = io.StringIO()
                        globalcounter += counter
                        counter = 0
                        bufferempty = True
                except:
                    tb = sys.exc_info()
                    message = str(tb[1])
                    logging.error(message)
                    error_queue.put(col)
                    hcache.rollback()
                    buffer = io.StringIO()
                    counter = 0
                    bufferempty = True
            if not bufferempty:
                try:
                    buffer.seek(0)
                    logging.info("Writing " + str(counter) + " records to collection: " + col + "...")
                    hcache.copy(buffer, col, tuple(tabledesc.keys()))
                    #hcache.commit()
                    globalcounter += counter
                except:
                    tb = sys.exc_info()
                    message = str(tb[1])
                    logging.error(message)
                    error_queue.put(col)
                    hcache.rollback()
            logging.info("Collection: " + col + ": " + str(globalcounter) + " records have been written! ")
            hcache.disconnect()

        try: limit = int(os.environ['PARALLEL'])
        except: limit = 0
        
        limit = multiprocessing.cpu_count() if limit==0 else limit

        try:
            pr = Parallel(read_from_queue, workers=1)
            pr.push(collection)
            pw = Parallel(write_to_queue, workers = limit)
            for p in producers: pw.push(p)
            pw.join()
            queue.put('KAIROS_DONE')
            pr.join()
            if not error_queue.empty():
                message = 'At least one error found during collection cache building! See KAIROS.LOG for more information!'
                status.error = message
            else:
                for producer in producers:
                    pnode = s.igetnodes(nodesdb=nodesdb, id=producer, getcache=True)[0]             
                    cache.collections[collection][str(pnode['id'])] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            queue.close()
            queue.join_thread()
            error_queue.close()
            error_queue.join_thread()
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status

    @trace_call
    def ibuildcolcachetypeB(s, node, cache=None, collections=None, analyzers=None, nodesdb=None):
        status = Object()
        status.error = None
        try:
            nid = node['id']
            queues = dict()
            writeheader = dict()
            readheader = dict()
            members = dict()
            queues['ERROR_QUEUE'] = multiprocessing.Queue()
            for collection in collections:
                queues[collection] = multiprocessing.Queue()
                writeheader[collection] = True
                readheader[collection] = True
                for member in node['datasource']['collections'][collection]['members']: members[member]=analyzers[collection]
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message

        def nulllistener(col, d, v, n): pass

        def write_to_queue(col, d, v, n):
            logging.debug('Writing to queue the following collection:' + col)
            if writeheader[col]:
                record = json.dumps(dict(header='KAIROS_START', desc=d)) 
                queues[col].put(record)
                writeheader[col] = False
            v = v if type(v) == type([]) else [v]
            for e in v:
                record = ''
                e['kairos_nodeid'] = nid
                for k in sorted(e.keys()): record += '\\N\t' if e[k] == '' else str(e[k]).replace('\n','\\n').replace('\t','\\t').replace('\r', '').replace('\\', '\\\\') + '\t'
                record = record[:-1] + '\n'
                queues[col].put(record)

        def read_from_queue(col):
            hcache = Cache(nodesdb, schema=cache.name)
            buffer = io.StringIO()
            bufferempty = True
            counter = 0
            try: limit = int(os.environ['BUFFER'])
            except: limit = 10000
            globalcounter = 0
            while True:
                try:
                    record = queues[col].get()
                    if record == 'KAIROS_DONE': break
                    try: record = json.loads(record)
                    except: pass
                    if type(record) == type(dict()) and 'header' in record and record['header'] == 'KAIROS_START':
                        if readheader[col]:
                            record['desc']['kairos_nodeid'] = 'text'
                            request = 'create table ' + col + '('
                            description= sorted(record['desc'].keys())
                            for k in description: request += k + ' ' + record['desc'][k] +  ', '
                            request = request[:-2] + ')'
                            hcache.execute(request)
                            #hcache.commit()
                            readheader[col] = False
                    else:
                        bufferempty = False
                        counter += 1
                        logging.debug('Buffer content at line: ' + str(counter) + ', record: ' + str(record))
                        buffer.write(record)
                        if counter == limit:
                            buffer.seek(0)
                            logging.info("Writing " + str(counter) + " records to collection: " + col + "...")
                            hcache.copy(buffer, col, tuple(description))
                            #hcache.commit()
                            buffer = io.StringIO()
                            globalcounter += counter
                            counter = 0
                            bufferempty = True
                except:
                    tb = sys.exc_info()
                    message = str(tb[1])
                    logging.error(message)
                    queues['ERROR_QUEUE'].put(col)
                    hcache.rollback()
                    buffer = io.StringIO()
                    counter = 0
                    bufferempty = True
            if not bufferempty:
                try:
                    buffer.seek(0)
                    logging.info("Writing " + str(counter) + " records to collection: " + col + "...")
                    hcache.copy(buffer, col, tuple(description))
                    #hcache.commit()
                    globalcounter += counter
                except:
                    tb = sys.exc_info()
                    message = str(tb[1])
                    queues['ERROR_QUEUE'].put(col)
                    logging.error(message)
                    hcache.rollback()
            logging.info("Collection: " + col + ": " + str(globalcounter) + " records have been written! ")
            hcache.disconnect()
        
        thezip = zipfile.ZipFile(io.BytesIO(node['datasource']['stream']))
        logging.info('Analyzing archive attached to node ' + str(nid) + '...')
        try: nolistener = eval(os.environ['NOLISTENER'])
        except: nolistener = False
        listen = nulllistener if nolistener else write_to_queue
        
        def do(member):
            if member in members:
                analyzer = Analyzer(members[member], set(collections), listen, nid)
                logging.info('Analyzing member: ' + member + '...')
                status = analyzer.analyze(thezip.read(member), member)
                if status.error: queues['ERROR_QUEUE'].put(member)
                return None
        try: limit = int(os.environ['PARALLEL'])
        except: limit = 0
        limit = multiprocessing.cpu_count() if limit==0 else limit

        try:
            pr = Parallel(read_from_queue, workers=len(collections))
            for collection in collections: pr.push(collection)
            pw = Parallel(do, workers = limit)
            for e in thezip.namelist(): pw.push(e)
            pw.join()
            thezip.close()
            for collection in collections: queues[collection].put('KAIROS_DONE')
            pr.join()
            if not queues['ERROR_QUEUE'].empty():
                message = 'At least one error found during collection cache building! See KAIROS.LOG for more information!'
                status.error = message
            else:
                for collection in collections: cache.collections[collection][str(nid)] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            for collection in collections: 
                queues[collection].close()
                queues[collection].join_thread()
            queues['ERROR_QUEUE'].close()
            queues['ERROR_QUEUE'].join_thread()
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status

    @trace_call
    def ibuildcolcachetypeD(s, node, cache=None, collection=None, nodesdb=None):
        status = Object()
        status.error = None
        try:
            nid = node['id']
            ntype = node['datasource']['type']
            logging.info("Node: " + str(nid) + ", Type: " + ntype + ", building new collection cache: '" + collection + "' ...")
            hcache = Cache(nodesdb, schema=cache.name)
            hcache.execute("create table " + collection + " as select '" + str(nid) + "'::text as kairos_nodeid, * from foreign_" +collection)
            hcache.disconnect()
            cache.collections[collection][str(nid)] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status

    @trace_call
    def icheckcollectioncache(s, node, cache=None, collections=None, nodesdb=None, systemdb=None):
        status = Object()
        status.error = None
        status.todo = dict()
        status.mapproducers = dict()
        status.analyzers = dict()
        try:
            nid = node['id']
            ntype = node['datasource']['type']
            if ntype in ['C', 'L']:
                for producer in node['datasource']['producers']:
                    pnode = s.igetnodes(nodesdb=nodesdb, id=producer['id'], getsource=True, getcache=True, getstream=True)[0]
                    bstatus = s.ibuildcollectioncache(pnode, collections=collections, systemdb=systemdb, nodesdb=nodesdb)
                    status.error = bstatus.error if bstatus.error else status.error
                for collection in collections: status.todo[collection] = False
            if ntype in ['A', 'B', 'D']:
                for collection in collections:
                    if collection not in cache.collections: cache.collections[collection] = dict()
            if ntype in ['A']: 
                astatus = s.icheckcolcachetypeA(node, cache=cache, collections=collections, nodesdb=nodesdb, systemdb=systemdb)
                status.error = astatus.error
                status.todo = astatus.todo
                status.mapproducers = astatus.mapproducers
            if ntype in ['B']: 
                bstatus = s.icheckcolcachetypeB(node, cache=cache, collections=collections, nodesdb=nodesdb, systemdb=systemdb)
                status.error = bstatus.error
                status.todo = bstatus.todo
                status.analyzers = bstatus.analyzers
            if ntype in ['D']: 
                dstatus = s.icheckcolcachetypeD(node, cache=cache, collections=collections, nodesdb=nodesdb, systemdb=systemdb)
                status.error = dstatus.error
                status.todo = dstatus.todo
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status

    @trace_call
    def ibuildcollectioncache(s, node, collections=None, nodesdb=None, systemdb=None):
        status = Object()
        status.error = None
        try:
            nid = node['id']
            ntype = node['datasource']['type']
            nodecache = node['datasource']['cache']
            if 'name' not in nodecache: s.icreatecache(nid, nodesdb=nodesdb)
            cache = s.igetcache(nid, nodesdb=nodesdb)
            if '*' in collections: collections = {k for k in node['datasource']['collections']}
            cstatus = s.icheckcollectioncache(node, cache=cache, collections=collections, nodesdb=nodesdb, systemdb=systemdb)
            status.error = cstatus.error if cstatus.error else status.error
            status.todo = cstatus.todo
            if True in status.todo.values():
                tcollections = [k for k in status.todo if status.todo[k]]
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", building collection cache: '" + str(tcollections) + "' ...")
                dbname = cache.name
                for collection in tcollections:
                    logging.info("Node: " + str(nid) + ", Type: " + ntype + ", removing obsolete parts of old collection cache: '" + collection + "' ...")
                    if ntype in ['A']: 
                        astatus = s.idropcolcachetypeA(node, mapproducers=cstatus.mapproducers, cache=cache, collection=collection, nodesdb=nodesdb)
                        status.error = astatus.error if astatus.error else status.error
                    if ntype in ['B']: 
                        bstatus = s.idropcolcachetypeB(node, cache=cache, collection=collection, nodesdb=nodesdb)
                        status.error = bstatus.error if bstatus.error else status.error
                    if ntype in ['D']: 
                        dstatus = s.idropcolcachetypeD(node, cache=cache, collection=collection, nodesdb=nodesdb)                
                        status.error = dstatus.error if dstatus.error else status.error
                for collection in tcollections:
                    if ntype in ['A']: 
                        astatus = s.ibuildcolcachetypeA(node, cache=cache, collection=collection, nodesdb=nodesdb, systemdb=systemdb, mapproducers=cstatus.mapproducers)
                        status.error = astatus.error if astatus.error else status.error
                    if ntype in ['D']: 
                        dstatus = s.ibuildcolcachetypeD(node, cache=cache, collection=collection, nodesdb=nodesdb)
                        status.error = dstatus.error if dstatus.error else status.error
                if ntype in ['B']: 
                    bstatus = s.ibuildcolcachetypeB(node, cache=cache, collections=tcollections, analyzers=cstatus.analyzers, nodesdb=nodesdb)
                    status.error = bstatus.error if bstatus.error else status.error
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", updating cache with collections info: '" + str(tcollections) + "' ...")
                ncache = Cache(nodesdb, autocommit=True)
                ncache.execute("update caches set collections = '" + json.dumps(cache.collections) + "' where id = " + str(nid))
                ncache.disconnect()
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status
    
    @trace_call
    def ibuildquerycache(s, node, query=None, nodesdb=None, systemdb=None):
        status = Object()
        status.error = None
        try:
            nid = node['id']
            qid = query['id']
            ntype = node['datasource']['type']
            logging.info("Node: " + str(nid) + ", Type: " + ntype + ", checking query cache: '" + qid + "' ...")
            cache = s.igetcache(nid, nodesdb=nodesdb)
            if ntype in ['C', 'L']:
                for producer in node['datasource']['producers']:
                    pnode = s.igetnodes(nodesdb=nodesdb, id=producer['id'], getsource=True, getcache=True)[0]
                    status = s.ibuildquerycache(pnode, query=query, systemdb=systemdb, nodesdb=nodesdb)
                    if status.error: return status
            if ntype in ['A', 'B', 'D']:
                todo = True if qid not in cache.queries else False
                todo = True if "nocache" in query and query["nocache"] else todo
                for collection in query['collections']:
                    for part in cache.collections[collection]:
                        todo = True if qid in cache.queries and cache.queries[qid] < cache.collections[collection][part] else todo
                if todo:
                    hcache = Cache(nodesdb, schema=cache.name)
                    table = qid
                    logging.info("Node: " + str(nid) + ", Type: " + ntype + ", removing old query cache: '" + qid + "' ...")
                    hcache.execute("drop table if exists " + table)
                    logging.info("Node: " + str(nid) + ", Type: " + ntype + ", building new query cache: '" + qid + "' ...")
                    if 'userfunctions' in query:
                        for ufn in query['userfunctions']:
                            uf = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + ufn + "' and type='function'")[0]
                            hcache.execute(uf["function"])
                    global kairos
                    kairos['node'] = node
                    hcache.execute("create table " + table + " as select * from (" + query['request'] + ") as foo")
                    cache.queries[qid] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    hcache.disconnect()
                    logging.info("Node: " + str(nid) + ", Type: " + ntype + ", updating cache with query info: '" + qid + "' ...")
                    ncache = Cache(nodesdb, autocommit=True)
                    ncache.execute("update caches set queries = '" + json.dumps(cache.queries) + "' where id = " + str(nid))
                    ncache.disconnect()
                else:
                    logging.info("Node: " + str(nid) + ", Type: " + ntype + ", nothing to do for query cache: '" + qid + "' ...")
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status
   
    @trace_call
    def iqueryexecute(s, node, query=None, nodesdb=None, limit=None):
        status = Object()
        status.error = None
        status.result = []
        try:
            nid = node['id']
            qid = query['id']
            ntype = node['datasource']['type']
            logging.info("Node: " + str(nid) + ", Type: " + ntype + ", executing query: '" + qid + "' ...")
            cache = s.igetcache(nid, nodesdb=nodesdb)
            if ntype in ['C', 'L']:
                for producer in node['datasource']['producers']:
                    pnode = s.igetnodes(nodesdb=nodesdb, id=producer['id'], getsource=True, getcache=True)[0]
                    estatus = s.iqueryexecute(pnode, query=query, nodesdb=nodesdb, limit=limit)
                    status.error = estatus.error if estatus.error else status.error
                    if ntype in ['L']: status.result = estatus.result
                    else: status.result.append(estatus.result)
            else:
                hcache = Cache(nodesdb, schema=cache.name)
                table = qid.lower()
                for b in hcache.execute("select exists(select * from information_schema.tables where table_schema = current_schema() and table_name = '" + table + "') foo"): existstable = b['foo']
                if existstable: 
                    if 'filterable' in query and query['filterable']:
                        for x in hcache.execute("select * from " + table + " where label in (select label from (select label, sum(value) weight from " + table + " group by label order by weight desc limit " + str(limit) + ") as foo)"):
                            status.result.append(x)
                    else:
                        for x in hcache.execute("select * from " + table):
                            status.result.append(x)
                hcache.disconnect()
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        return status
  
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
        postgresstr = "host='localhost' dbname='kairos_user_" + user + "' user='" + user + "' password='" + password + "'"
        try: 
            postgres = psycopg2.connect(postgresstr)
            postgres.close()
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
            ncache = Cache(database, autocommit=True)
            ncache.execute("delete from objects where id='" + str(id) + "' and type='" + typeobj + "'")
            ncache.executep("insert into objects(rid, id, type, created, filename, stream) values (nextval('objid'), %s, %s, now(), %s, %s)", (id, typeobj, filename, content))
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
        ncache = Cache(db)
        y = ncache.execute("select top, colors, logging, nodesdb, systemdb, template, wallpaper, plotorientation from settings")
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
        data = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="where type='template'")
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listaggregators(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        data = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="where type='aggregator'")
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listliveobjects(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        data = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="where type='liveobject'")
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listwallpapers(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        data = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="where type='wallpaper'")
        return web.json_response(dict(success=True, data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listcolors(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        data = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="where type='color'")
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
        ncache = Cache(database)
        y = ncache.execute("select stream from objects where id='" + str(objid) +"' and type = '" + objtype + "'")
        result = dict()
        for row in y.fetchall():
            for x in row.keys(): result[x] = row[x]
        ncache.disconnect()
        source = binascii.a2b_base64(result['stream'])
        return web.json_response(dict(success=True, data=source.decode()))

    @intercept_logging_and_internal_error
    @trace_call
    def updatesettings(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        template = params['template'][0]
        colors = params['colors'][0]
        wallpaper = params['wallpaper'][0]
        top = params['top'][0]
        plotorientation = params['plotorientation'][0]
        logging = params['logging'][0]
        db = "kairos_user_" + user
        ncache = Cache(db, autocommit=True)
        ncache.execute("delete from settings")
        ncache.execute("insert into settings(colors, logging, nodesdb, plotorientation, systemdb, template, top, wallpaper) values ('" + colors +"', '" + logging +"', '" + nodesdb +"', '" + plotorientation + "', '" + systemdb + "', '" + template + "', " + str(top) + ", '" + wallpaper + "')")
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
        ncache = Cache(nodesdb, autocommit=True)
        ncache.execute("delete from objects where id='" + str(id) + "' and type='" + typeobj +"'")
        ncache.executep("insert into objects(rid, id, type, created, filename, stream) values (nextval('objid'), %s, %s, now(), %s, %s)", (id, typeobj, filename, content))
        ncache.disconnect()
        return web.json_response(dict(success=True, state=True, name=filename, id=id, type=typeobj))

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
        s.icreatesource(id, nodesdb=nodesdb, systemdb=systemdb, stream=upload.file, filename=filename)
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
        postgresstr = "host='localhost' dbname='kairos_user_" + user + "' user='" + user + "' password='" + password + "'"
        try: 
            postgres = psycopg2.connect(postgresstr)
            postgres.close()
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
        ncache = Cache(database, autocommit=True)
        ncache.execute("delete from objects where id='" + str(id) + "' and type='" + typeobj + "'")
        ncache.disconnect()
        return web.json_response(dict(success=True, data=dict(msg=id + ' ' + typeobj + ' object has been successfully removed!')))

    @intercept_logging_and_internal_error
    @trace_call
    def downloadobject(s, request):
        params = parse_qs(request.query_string)
        database = params['database'][0]
        id = params['id'][0]
        typeobj = params['type'][0]
        ncache = Cache(database, autocommit=True)
        y = ncache.execute("select filename, stream as content from objects where id = '" + str(id) + "' and type = '" + typeobj + "'")
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
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getstream=True)[0]
        filename = s.igetpath(nodesdb=nodesdb, id=id)[1:].replace('/','_')+'.zip'
        return web.Response(headers=MultiDict({'Content-Disposition': 'Attachment;filename="' + filename + '"'}), body=node['datasource']['stream'])

    @intercept_logging_and_internal_error
    @trace_call
    def getBchildren(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        ncache = Cache(nodesdb, autocommit=True)
        x = ncache.execute("with recursive tree as (select id, parent, type from nodes where id = " + str(id) + " union all select p.id, p.parent, p.type from nodes p join tree c on p.parent = c.id) select id as rid from tree where type='B'")
        listn = [row['rid'] for row in x.fetchall()]
        ncache.disconnect()
        return web.json_response(dict(success=True, data=listn))

    @intercept_logging_and_internal_error
    @trace_call
    def getmemberlist(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getstream=True)[0]
        thezip = zipfile.ZipFile(io.BytesIO(node['datasource']['stream']))
        listm = [dict(label=x) for x in thezip.namelist()]
        return web.json_response(dict(success=True, data=listm))

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
            liveobject = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + loname + "' and type='liveobject'")[0]
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
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getstream=True)[0]
        thezip = zipfile.ZipFile(io.BytesIO(node['datasource']['stream']))
        stream = thezip.read(member)
        type = magic.from_buffer(stream)
        stream = stream.decode().replace('#=', '# =').replace('#+', '# +')
        if 'html' in type.lower(): html = stream
        elif 'text' in type.lower(): html = '<pre>' + cgi.escape(stream) + '</pre>'
        else: html = 'Not yet taken into account'
        return web.json_response(dict(success=True, data=html))

    @intercept_logging_and_internal_error
    @trace_call
    def getmenus(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        data = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where type = 'menu'")
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
            result = [dict(kids=True, id=root['id'], text='/', userdata=dict(type=ftype(root)), icons=dict(file=icon_file, folder_opened=icon_opened, folder_closed=icon_closed))]
        else:
            children = []
            getkey = lambda x: x['text']
            for node in s.igetnodes(nodesdb=nodesdb, parent=parent, countchildren=True):
                (icon_file, icon_opened, icon_closed) = ficon(node)
                kids = True if node['kids'] > 0 else False
                children.append(dict(kids=kids, id=node['id'], text=node['name'], userdata=dict(type=ftype(node)), icons=dict(file=icon_file, folder_opened=icon_opened, folder_closed=icon_closed)))
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
        ncache = Cache(nodesdb, autocommit=True)
        x = ncache.execute("select parent as pid from nodes where id = " + str(id))
        parent=[row['pid'] for row in x.fetchall()][0]
        x = s.igetnodes(nodesdb=nodesdb, parent=parent, name=new)
        if len(x):
            message = new + " name already exists for parent: " + x[0]['name']
            ncache.disconnect()
            return web.json_response(dict(success=False, status='error', message=message))
        ncache.execute("update nodes set name = '" + new + "' where id = " + str(id))
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
        ncache = Cache(nodesdb, autocommit=True)
        x = ncache.execute("with recursive tree as (select id, parent from nodes where id = " + str(trash['id']) + " union all select p.id, p.parent from nodes p join tree c on p.parent = c.id) select id as rid from tree")
        listnodes = [row['rid'] for row in x.fetchall()]
        for rid in listnodes:
            s.ideletesource(rid, nodesdb=nodesdb, context=ncache)
            s.ideletecache(rid, nodesdb=nodesdb, context=ncache)
        ncache.execute("with recursive tree as (select id, parent from nodes where id = " + str(trash['id']) + " union all select p.id, p.parent from nodes p join tree c on p.parent = c.id) delete from nodes where id in (select id from tree where id != " + str(trash['id']) + ")")
        ncache.disconnect()
        return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    def movenode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        pfrom = params['from'][0]
        pto = params['to'][0]
        fromnode = s.igetnodes(nodesdb=nodesdb, id=pfrom)[0]
        if fromnode['datasource']['type'] == 'T':
            message = 'A trash cannot be moved!'
            return web.json_response(dict(success=False, status='error', message=message))
        tonode = s.igetnodes(nodesdb=nodesdb, id=pto)[0]
        ncache = Cache(nodesdb, autocommit=True)
        ncache.execute("update nodes set parent = " + str(pto) + " where id = "  + str(pfrom)) 
        x = ncache.execute("select status from nodes where id = " + str(pto))
        status = [row['status'] for row in x.fetchall()][0]
        ncache.execute("with recursive tree as (select id, parent from nodes where id = " + str(pfrom) + " union all select p.id, p.parent from nodes p join tree c on p.parent = c.id) update nodes set status = '" + status + "' where id in (select id from tree)")
        ncache.disconnect()
        node = s.igetnodes(nodesdb=nodesdb, id=pfrom)[0]
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
        chart = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + chart + "' and type='chart'")[0]
        return web.json_response(dict(success=True, data=chart))

    @intercept_logging_and_internal_error
    @trace_call
    def getjsonobject(s, request):
        params = parse_qs(request.query_string)
        database = params['database'][0]
        id = params['id'][0]
        type = params['type'][0]
        obj = s.igetobjects(nodesdb=database, systemdb=database, where="where id = '" + str(id) + "' and type = '" + type + "'", evalobject=False)[0]
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
        layout = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + layout + "' and type='layout'")[0]
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
        choice = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + choice + "' and type='choice'")[0]
        return web.json_response(dict(success=True, data=choice))

    @intercept_logging_and_internal_error
    @trace_call
    def gettemplate(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        template = params['template'][0]
        template = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + template + "' and type='template'")[0]
        return web.json_response(dict(success=True, data=template))

    @intercept_logging_and_internal_error
    @trace_call
    def getcolors(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        colors = params['colors'][0]
        colors = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + colors + "' and type='color'")[0]
        return web.json_response(dict(success=True, data=colors))

    @intercept_logging_and_internal_error
    @trace_call
    def getqueries(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        queries = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="where type='query'")
        return web.json_response(dict(success=True, data=queries))

    @intercept_logging_and_internal_error
    @trace_call
    def getcharts(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        charts = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="where type='chart'")
        return web.json_response(dict(success=True, data=charts))

    @intercept_logging_and_internal_error
    @trace_call
    def getchoices(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        choices = s.ilistobjects(nodesdb=nodesdb, systemdb=systemdb, where="where type='choice'")
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
        status = s.iexecutequery(nodesdb=nodesdb, systemdb=systemdb, id=id, query=query, limit=limit, variables=variables)
        if status.error: return web.json_response(dict(success=False, status='error', message=status.error))
        else: return web.json_response(dict(success=True, data=status.result))

    @intercept_logging_and_internal_error
    @trace_call
    def displaycollection(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        collection = params['collection'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True, getstream=True)[0]
        status = s.ibuildcollectioncache(node, collections=[collection], systemdb=systemdb, nodesdb=nodesdb)
        if status.error: return web.json_response(dict(success=False, status='error', message=status.error))
        status = s.iqueryexecute(node, query=dict(id=collection), nodesdb=nodesdb)
        if status.error: return web.json_response(dict(success=False, status='error', message=status.error))
        else: return web.json_response(dict(success=True, data=status.result))

    @intercept_logging_and_internal_error
    @trace_call
    def buildcollectioncache(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        collection = params['collection'][0]
        id = params['id'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True, getstream=True)[0]
        status = s.ibuildcollectioncache(node, collections={collection}, systemdb=systemdb, nodesdb=nodesdb)
        if status.error: return web.json_response(dict(success=False, status='error', message=status.error))
        else: return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    def buildallcollectioncaches(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True, getstream=True)[0]
        status = s.ibuildcollectioncache(node, collections={'*'}, systemdb=systemdb, nodesdb=nodesdb)
        if status.error: return web.json_response(dict(success=False, status='error', message=status.error))
        else: return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    def clearcollectioncache(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        status = s.ideletecache(id, nodesdb=nodesdb, context=None)
        if status.error: return web.json_response(dict(success=False, status='error', message=status.error))
        else: return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    def dropcollectioncache(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0] 
        collection = params['collection'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        status = s.idropcollectioncache(node, collection=collection, nodesdb=nodesdb)
        if status.error: return web.json_response(dict(success=False, status='error', message=status.error))
        else: return web.json_response(dict(success=True))

    @intercept_logging_and_internal_error
    @trace_call
    def compareaddnode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        fromid = int(params['from'][0])
        toid = int(params['to'][0])
        fnode = s.igetnodes(nodesdb=nodesdb, id=fromid)[0]
        tnode = s.igetnodes(nodesdb=nodesdb, id=toid)[0]
        if fnode['status'] == 'DELETED' or tnode['status'] == 'DELETED':
            message = 'A deleted element cannot be part of a compare operation!'
            return web.json_response(dict(success=False, status='error', message=message))
        for e in tnode['datasource']['producers']:
            if fromid == e['id']:
                message = str(fromid) + ": this node is already included in the list of producers!"
                return web.json_response(dict(success=False, status='error', message=message))
        producers = tnode['datasource']['producers']
        producers.append(dict(path=s.igetpath(nodesdb=nodesdb, id=fromid), id=fromid))
        ncache = Cache(nodesdb, autocommit=True)
        ncache.execute("update nodes set type='C', icon='C', producers='" + json.dumps(producers) + "' where id =" + str(toid))
        ncache.disconnect()
        tnode = s.igetnodes(nodesdb=nodesdb, id=toid, getsource=True)[0]
        return web.json_response(dict(success=True, data=tnode))
    
    @intercept_logging_and_internal_error
    @trace_call
    def aggregateaddnode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        fromid = int(params['from'][0])
        toid = int(params['to'][0])
        fnode = s.igetnodes(nodesdb=nodesdb, id=fromid)[0]
        tnode = s.igetnodes(nodesdb=nodesdb, id=toid)[0]
        if fnode['status'] == 'DELETED' or tnode['status'] == 'DELETED':
            message = 'A deleted element cannot be part of an aggreagte operation!'
            return web.json_response(dict(success=False, status='error', message=message))
        for e in tnode['datasource']['producers']:
            if fromid == e['id']:
                message = str(fromid) + ": this node is already included in the list of producers!"
                return web.json_response(dict(success=False, status='error', message=message))
        producers = tnode['datasource']['producers']
        producers.append(dict(path=s.igetpath(nodesdb=nodesdb, id=fromid), id=fromid))
        ncache = Cache(nodesdb, autocommit=True)
        if 'aggregatorselector' not in tnode['datasource']:
            ncache.execute("update nodes set type='A', icon='A', producers='" + json.dumps(producers) + "', aggregated=now(), aggregatorselector='" + s.igetpath(nodesdb=nodesdb, id=fromid) + '$' + "', aggregatortake=1, aggregatortimefilter='.', aggregatorskip=0, aggregatorsort='desc', aggregatormethod='$none' where id =" + str(toid))
        else:
            ncache.execute("update nodes set producers='" + json.dumps(producers) + "', aggregated=now(), aggregatorselector='" + tnode['datasource']['aggregatorselector'] + '|' + s.igetpath(nodesdb=nodesdb, id=fromid) + '$' +"', aggregatortake=" + str(int(tnode['datasource']['aggregatortake']) +  1) + " where id =" + str(toid))
        ncache.disconnect()
        tnode = s.igetnodes(nodesdb=nodesdb, id=toid, getsource=True)[0]
        return web.json_response(dict(success=True, data=tnode))
    
    @intercept_logging_and_internal_error
    @trace_call
    def applyaggregator(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = int(params['id'][0])
        aggregatorselector = params['aggregatorselector'][0]
        aggregatortake = int(params['aggregatortake'][0])
        aggregatorskip = int(params['aggregatorskip'][0])
        aggregatortimefilter = params['aggregatortimefilter'][0]
        aggregatorsort = params['aggregatorsort'][0]
        aggregatormethod = params['aggregatormethod'][0]
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        if node['datasource']['type'] in ['A']:
            if node['datasource']['aggregatormethod'] != aggregatormethod or node['datasource']['aggregatortimefilter'] != aggregatortimefilter:
                logging.info("Node: " + str(id) + ", Type: " + node['datasource']['type'] + ", deleting cache ...")
                s.ideletecache(id, nodesdb=nodesdb, context=None)
        if node['datasource']['type'] in ['A', 'N']:  
            producers = s.iexpand(pattern=aggregatorselector, nodesdb=nodesdb, sort=aggregatorsort, take=aggregatortake, skip=aggregatorskip)
            ncache = Cache(nodesdb, autocommit=True)
            ncache.execute("update nodes set type='A', icon='A', producers='" + json.dumps(producers) + "', aggregated=now(), aggregatorselector='" + aggregatorselector + "', aggregatortake=" + str(aggregatortake) + ", aggregatortimefilter='" + aggregatortimefilter + "', aggregatorskip=" + str(aggregatorskip) + ", aggregatorsort='" + aggregatorsort + "', aggregatormethod='" + aggregatormethod + "' where id =" + str(id))
            ncache.disconnect()
        if node['datasource']['type'] in ['L']:
            cproducers = dict()
            producers = s.iexpand(pattern=aggregatorselector, nodesdb=nodesdb, sort=aggregatorsort, take=aggregatortake, skip=aggregatorskip)
            ncache = Cache(nodesdb, autocommit=True)
            ncache.execute("update nodes set type='L', icon='L', producers='" + json.dumps(producers) + "', aggregated=now(), aggregatorselector='" + aggregatorselector + "', aggregatortake=" + str(aggregatortake) + ", aggregatortimefilter='" + aggregatortimefilter + "', aggregatorskip=" + str(aggregatorskip) + ", aggregatorsort='" + aggregatorsort + "', aggregatormethod='" + aggregatormethod + "' where id =" + str(id))
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
                logging.info("Node: " + str(id) + ", Type: " + node['datasource']['type'] + ", deleting obsolete child: '" + e + "' ...")
                s.ideletenode(id=e, nodesdb=nodesdb)
            for n in pnames - nnames:
                logging.info("Node: " + str(id) + ", Type: " + node['datasource']['type'] + ", creating new child: '" + n + "' ...")
                s.icreatenode(id=node['id'], nodesdb=nodesdb, name=n)
            nchilds = s.igetnodes(nodesdb=nodesdb, parent=node['id'])
            for c in nchilds:
                if 'aggregatormethod' in c['datasource'] and 'aggregatortimefilter' in c['datasource']:
                    if c['datasource']['aggregatormethod'] != aggregatormethod or c['datasource']['aggregatortimefilter'] != aggregatortimefilter:
                        logging.info("Node: " + str(c['id'])+ ", Type: " + c['datasource']['type'] + ", deleting cache if exists ...")
                        s.ideletecache(c['id'], nodesdb=nodesdb)
                tpath = [x['path'] for x in cproducers[c['name']]]
                aggregatorselector = '|'.join(tpath)
                ncache = Cache(nodesdb, autocommit=True)
                ncache.execute("update nodes set type='A', icon='A', producers='" + json.dumps(cproducers[c['name']]) + "', aggregated=now(), aggregatorselector='" + aggregatorselector + "', aggregatortake=" + str(aggregatortake) + ", aggregatortimefilter='" + aggregatortimefilter + "', aggregatorskip=" + str(aggregatorskip) + ", aggregatorsort='" + aggregatorsort + "', aggregatormethod='" + aggregatormethod + "' where id =" + str(c['id']))
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
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True, getstream=True)[0]
        path = s.igetpath(nodesdb=nodesdb, id=id)
        archive = path.replace('/', '_')[1:] + '-unload.zip'
        fname = '/tmp/' + archive
        zip = Arcfile(fname, 'w:zip')
        cut = 10000
        done = s.ibuildcollectioncache(node, collections={'*'}, systemdb=systemdb, nodesdb=nodesdb)
        status = s.ibuildcollectioncache(node, collections={'*'}, systemdb=systemdb, nodesdb=nodesdb)
        done = status.todo
        node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True)[0]        
        hcache = Cache(nodesdb, schema=node['datasource']['cache']['name'])
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
        nodesdb = params['nodesdb'][0]
        fromid = int(params['from'][0])
        toid = int(params['to'][0])
        fnode = s.igetnodes(nodesdb=nodesdb, id=fromid)[0]
        tnode = s.igetnodes(nodesdb=nodesdb, id=toid)[0]
        fpath = s.igetpath(id=fromid, nodesdb=nodesdb)
        if fnode['status'] == 'DELETED' or tnode['status'] == 'DELETED':
            message = 'A trash cannot be part of a link operation!'
            return web.json_response(dict(success=False, status='error', message=message))
        producers = tnode['datasource']['producers']
        if fromid in [producer['id'] for producer in producers]:
            message = fpath + ': this node is already included in the list of producers!'
            return web.json_response(dict(success=False, status='error', message=message))   
        producers.append(dict(path=s.igetpath(nodesdb=nodesdb, id=fromid), id=fromid))
        ncache = Cache(nodesdb, autocommit=True)
        if 'aggregatorselector' not in tnode['datasource']:
            ncache.execute("update nodes set type='L', icon='L', producers='" + json.dumps(producers) + "', aggregated=now(), aggregatorselector='" + s.igetpath(nodesdb=nodesdb, id=fromid) + '$' + "', aggregatortake=1, aggregatortimefilter='.', aggregatorskip=0, aggregatorsort='desc', aggregatormethod='$none' where id =" + str(toid))
        else:
            ncache.execute("update nodes set producers='" + json.dumps(producers) + "', aggregated=now(), aggregatorselector='" + tnode['datasource']['aggregatorselector'] + '|' + s.igetpath(nodesdb=nodesdb, id=fromid) + '$' +"', aggregatortake=" + str(int(tnode['datasource']['aggregatortake']) +  1) + " where id =" + str(toid))
        ncache.disconnect()
        tnode = s.igetnodes(nodesdb=nodesdb, id=toid, getsource=True)[0]
        return web.json_response(dict(success=True, data=tnode))

    @intercept_logging_and_internal_error
    @trace_call
    def applyliveobject(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        loname = params['liveobject'][0]
        id = int(params['id'][0])
        liveobject = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + loname + "' and type='liveobject'")[0]
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        if node['datasource']['type'] in ['D']:
            logging.info("Node: " + str(id) + ", Type: " + node['datasource']['type'] + ", deleting cache ...")
            s.ideletecache(id, nodesdb=nodesdb, context=None)
        s.icreatecache(id, nodesdb=nodesdb)
        cache = s.igetcache(id, nodesdb=nodesdb)
        (message, collections) = s.iapplyliveobject(id=id, cache=cache, liveobject=liveobject, nodesdb=nodesdb)
        ncache = Cache(nodesdb, autocommit=True)
        ncache.execute("update nodes set type='D', icon='D', aggregated=now(), liveobject='" + loname + "' where id = " + str(id))
        ncache.disconnect()
        node = s.igetnodes(nodesdb=nodesdb, id=id)[0]
        if message: return web.json_response(dict(success=False, message=message))
        else: return web.json_response(dict(success=True, data=node))

    @intercept_logging_and_internal_error
    @trace_call
    def exportdatabase(s, request):
        params = parse_qs(request.query_string)
        nodesdb = [params['nodesdb'][0]] if 'nodesdb' in params else []
        gerrors = 0
        experr = 0
        if len(nodesdb) == 0:
            ncache = Cache(None, autocommit=True)
            x = ncache.execute("select datname from pg_database where datname like 'kairos_user_%' or datname like 'kairos_group_%'")
            nodesdb = [row['datname'] for row in x.fetchall()]
            ncache.disconnect()
        for db in nodesdb:
            try: shutil.rmtree('/export/' + db)
            except: pass
            os.mkdir('/export/' + db)
            os.chmod('/export/' + db, 0o777)
            logging.info("Trying to export database " + db + " ...")
            ag = subprocess.run(['su', '-', 'postgres', '-c', 'pg_dump -F c -f /export/' + db + '/database.dump ' + db], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if  ag.returncode:
                message = "Unable to export database: " + db + " for an uknown reason!"
                experr += 1
                logging.error(message)
                continue
        if experr > 0: return web.json_response(dict(success=False, data=dict(msg= str(experr) + " database(s) has(ve) not been exported!")))
        elif gerrors == 0: return web.json_response(dict(success=True, data=dict(msg="Database(s): " + str(nodesdb) + " has(ve) been exported sucessfully!")))
        else: return web.json_response(dict(success=True, data=dict(msg="Database(s): " + str(nodesdb) + " has(ve) been exported but " + str(gerrors) + " error(s) has(ve) been met while exporting files!")))

    @intercept_logging_and_internal_error
    @trace_call
    def importdatabase(s, request):
        params = parse_qs(request.query_string)
        nodesdb = [params['nodesdb'][0]] if 'nodesdb' in params else []
        gerrors = 0
        imperr = 0
        if len(nodesdb) == 0:
            for d in os.listdir('/export'):
                wdir = '/export/' + d
                if 'kairos_' in d and os.path.isdir(wdir): nodesdb.append(d)
        for db in nodesdb:
            logging.info("Trying to import database " + db + " ...")
            logging.info("Trying to drop database " + db + "...")
            ag = subprocess.run(['su', '-', 'postgres', '-c', 'psql -c "drop database ' + db + '"'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if  ag.returncode:
                message = "Unable to drop database: " + db + " during import!"
                logging.error(message)
                imperr += 1
                continue
            logging.info("Trying to create database " + db + "...")
            ag = subprocess.run(['su', '-', 'postgres', '-c', 'psql -c "create database ' + db + '"'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if  ag.returncode:
                message = "Unable to create database: " + db + " during import!"
                logging.error(message)
                imperr += 1
                continue
            logging.info("Trying to restore database " + db + "...")
            ag = subprocess.run(['su', '-', 'postgres', '-c', 'pg_restore -d ' + db + ' /export/' + db + '/database.dump'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if  ag.returncode:
                message = "Error during import of database: " + db
                logging.error(message)
                imperr += 1
                continue
        if imperr > 0: return web.json_response(dict(success=False, data=dict(msg= str(imperr) + " database(s) has(ve) not been imported!")))
        elif gerrors == 0: return web.json_response(dict(success=True, data=dict(msg="Database(s): " + str(nodesdb) + " has(ve) been imported sucessfully!")))
        else: return web.json_response(dict(success=True, data=dict(msg="Database(s): " + str(nodesdb) + " has(ve) been imported but " + str(gerrors) + " error(s) has(ve) been met while importing files!")))

    @trace_call
    def cleardependentcaches(s, request):
        status = Object()
        status.error = None
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        try:
            ncache = Cache(nodesdb, autocommit=True)
            x = ncache.execute("with recursive tree as (select id, parent, type from nodes where id = " + str(id) + " union all select p.id, p.parent, p.type from nodes p join tree c on p.parent = c.id) select id as rid from tree where type in ('A', 'B')")
            dependents = [row['rid'] for row in x.fetchall()]
            ncache.disconnect()
            for n in dependents:
                estatus = s.ideletecache(n, nodesdb=nodesdb, context=None)
                status.error = estatus.error if estatus.error else status.error
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        if status.error: return web.json_response(dict(success=False, message="Caches may been cleared with errors!"))
        else: return web.json_response(dict(success=True, data=dict(msg="Caches have been cleared sucessfully!")))

    @trace_call
    def clearmemorycaches(s, request):
        status = Object()
        status.error = None
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = int(params['id'][0])
        try:
            memorycache = MemoryCache(('localhost', 11211))
            memorycache.flush(id)
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        if status.error: return web.json_response(dict(success=False, message="Node: " + str(id) + " - memory cache may have been cleared with errors!"))
        else: return web.json_response(dict(success=True, data=dict(msg="Node: " + str(id) + " - memory cache has been cleared sucessfully!")))

    @trace_call
    def builddependentcaches(s, request):
        status = Object()
        status.error = None
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        try:
            ncache = Cache(nodesdb, autocommit=True)
            x = ncache.execute("with recursive tree as (select id, parent, type from nodes where id = " + str(id) + " union all select p.id, p.parent, p.type from nodes p join tree c on p.parent = c.id) select id as rid from tree where type in ('A', 'B')")
            dependents = [row['rid'] for row in x.fetchall()]
            ncache.disconnect()
            for n in dependents:
                node = s.igetnodes(nodesdb=nodesdb, id=n, getsource=True, getcache=True, getstream=True)[0]
                bstatus = s.ibuildcollectioncache(node, collections={'*'}, systemdb=systemdb, nodesdb=nodesdb)
                if bstatus.error: 
                    message = "Error while trying to build cache for node: " + n
                    logging.error(message)
                    logging.error(bstatus.error)
                    status.error = bstatus.error
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        if status.error: return web.json_response(dict(success=False, message="Caches may have been built with errors!"))
        else: return web.json_response(dict(success=True, data=dict(msg="Caches have been built sucessfully!")))
    @intercept_logging_and_internal_error
    @trace_call
    def runchart(s, request):
        status = Object()
        status.error = None
        params = parse_qs(request.query_string)
        try:
            nodesdb = params['nodesdb'][0]
            systemdb = params['systemdb'][0]
            id = int(params['id'][0])
            chart = params['chart'][0]
            width = int(params['width'][0])
            height = int(params['height'][0])
            limit = int(params['top'][0])
            colors = params['colors'][0]
            plotorientation = params['plotorientation'][0]
            template = params['template'][0]
            variables = json.loads(params['variables'][0])
            for v in variables: kairos[v] = variables[v]
            node = s.igetnodes(nodesdb=nodesdb, id=id, getsource=True, getcache=True, getstream=True)[0]
            timeout = 3600
            if node['datasource']['type'] == 'D':
                liveobject = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + node['datasource']['liveobject'] + "' and type='liveobject'")[0]
                try: timeout = liveobject['retention']
                except: timeout = 60
            memorycache = MemoryCache(('localhost', 11211), timeout)
            memorykey = dict(nodesdb=nodesdb, systemdb=systemdb, id=id, chart=chart, limit=limit, colors=colors, plotorientation=plotorientation, variables=variables, template=template)
            jsonchart = memorycache.get(memorykey)
            if jsonchart:
                chartobj = json.loads(jsonchart)
                fig = chartobj['figure']
                rows = chartobj['rows']
            else:
                template = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + template + "' and type='template'")[0]
                colors = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + colors + "' and type='color'")[0]['colors']
                getcolor = lambda x: colors[x] if x in colors else '#' + hashlib.md5(x.encode('utf-8')).hexdigest()[0:6]
                chart = s.igetobjects(nodesdb=nodesdb, systemdb=systemdb, where="where id='" + chart + "' and type='chart'")[0]
                producers = [k['path'] for k in node['datasource']['producers']] if 'producers' in node['datasource'] and node['datasource']['type'] == 'C' else []
                co=dict(rows=1, cols=1, isarray=False, shared_yaxes=False, shared_xaxes=False, layoutoptions=dict(), xaxis=dict(), yaxis=dict(), alreadyright=dict(), alreadyleft=dict(), traces=dict(), pies=dict())
                status = s.iexecutequery(nodesdb=nodesdb, systemdb=systemdb, id=id, query=chart['reftime'], limit=limit, variables=variables)
                if status.error: return web.json_response(dict(success=False, status='error', message=status.error))
                reftimedf = gettimestampdf(status.result, co, plotorientation)
                co['shared_yaxes'] = True if plotorientation == 'horizontal' else False
                co['shared_xaxes'] = True if plotorientation == 'vertical' else False
                getnewaxis(co, reftimedf, template, axistype='x', index=0)
                if co['shared_yaxes']:
                    i = 1
                    for e in reftimedf[1:]: 
                        getnewaxis(co, reftimedf, template, axistype='x', index=i)
                        i += 1
                    co['cols'] = i
                if co['shared_xaxes']: co['rows'] = len(reftimedf)
                fig = plotly.subplots.make_subplots(rows=co['rows'], cols=co['cols'], shared_yaxes=co['shared_yaxes'], shared_xaxes=co['shared_xaxes'], subplot_titles=tuple(producers))
                for e in template['layout']: co['layoutoptions'][e] = template['layout'][e].copy() if type(template['layout'][e]) == type(dict()) else template['layout'][e]
                co['layoutoptions']['title']['text'] = chart['title']
                co['layoutoptions']['width'] = width
                co['numyaxis'] = 0
                events = dict()
                for y in chart['yaxis']:
                    co['numyaxis'] += 1
                    idxy = []
                    if co['shared_yaxes']: 
                        idxy.append(getnewaxis(co, reftimedf, template, axistype='y', options=y, index=0))
                    else:
                        for i in range(co['rows']): idxy.append(getnewaxis(co, reftimedf, template, axistype='y', options=y, index=i))
                    for r in y['renderers']:
                        co['pielabels'] = dict()
                        co['pievalues'] = dict()
                        co['piecolors'] = dict()
                        for d in r['datasets']:
                            alreadyinlegend = dict()
                            status = s.iexecutequery(nodesdb=nodesdb, systemdb=systemdb, id=id, query=d['query'], limit=limit, variables=variables)
                            if status.error: return web.json_response(dict(success=False, status='error', message=status.error))
                            datasetdf = gettimestampdf(status.result, co, plotorientation)
                            labeldf = [x.groupby('label')[['value']].sum() for x in datasetdf]
                            ascending = 0
                            i = 0
                            for e in labeldf:
                                if i not in co['pielabels']: co['pielabels'][i] = []
                                if i not in co['pievalues']: co['pievalues'][i] = []
                                if i not in co['piecolors']: co['piecolors'][i] = []
                                for label, row in e.sort_values(by=['value'], ascending=ascending).iterrows():
                                    events[label] = dict(info=None, onclick=None)
                                    if 'onclick' in d and d['onclick']: events[label]['onclick'] = d['onclick']
                                    if 'info' in d and d['info']: events[label]['info'] = d['info']
                                    if r['type'] == 'P':
                                        co['pielabels'][i].append(label)
                                        co['pievalues'][i].append(row['value'])
                                        co['piecolors'][i].append(getcolor(label))
                                    else:
                                        paddeddatasetdf = paddeddf(reftimedf[i], datasetdf[i][datasetdf[i]['label'] == label])
                                        settrace(co, r, dataframe=paddeddatasetdf, label=label, yaxisindex=idxy[i] if co['shared_xaxes'] else idxy[0], index=i, alreadyinlegend=alreadyinlegend, groupname=getcolor(str(r)), plotorientation=plotorientation, colors=colors)
                                i += 1
                    if r['type'] == 'P':
                        for i in co['pielabels']:
                            co['pies'][i]=dict(trace=plotly.graph_objs.Pie(labels=co['pielabels'][i], values=co['pievalues'][i], hoverinfo='label+percent', textinfo='none', marker=dict(colors=co['piecolors'][i], line=dict(color='#000000', width=2))), row=1, col=i)
                if len(co['pies']) > 0:
                    fig['layout'].update(**co['layoutoptions'])
                    fig = json.loads(json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder))
                    for i in co['pies']:
                        fig['data'].append(json.loads(json.dumps(co['pies'][i]['trace'], cls=plotly.utils.PlotlyJSONEncoder)))
                else:
                    for it in co['pies']: fig.append_trace(co['pies'][it]['trace'], co['pies'][it]['row'], co['pies'][it]['col'])
                    for it in co['traces']: fig.append_trace(co['traces'][it]['trace'], co['traces'][it]['row'], co['traces'][it]['col'])
                    for it in co['traces']: fig['data'][it].update(xaxis=co['xaxis'][co['traces'][it]['xaxis']]['smallname'], yaxis=co['yaxis'][co['traces'][it]['yaxis']]['smallname'])
                    for iy in co['yaxis']: setattr(fig['layout'], co['yaxis'][iy]['name'], plotly.graph_objs.layout.YAxis())
                    for ix in co['xaxis']: setattr(fig['layout'], co['xaxis'][ix]['name'], plotly.graph_objs.layout.XAxis())
                    fig['layout'].update(**co['layoutoptions'])
                    for iy in co['yaxis']: fig['layout'][co['yaxis'][iy]['name']].update(**co['yaxis'][iy]['options'])
                    for ix in co['xaxis']: fig['layout'][co['xaxis'][ix]['name']].update(**co['xaxis'][ix]['options'])
                rows = co['rows']
                chartobj = dict(figure=fig, events=events, rows=rows)
                memoryvalue = json.dumps(chartobj, cls=plotly.utils.PlotlyJSONEncoder)
                try: memorycache.set(memorykey, memoryvalue)
                except: pass
                chartobj = json.loads(memoryvalue)
                fig = chartobj['figure']
            fig['layout']['width'] = width
            if 'titlefont' not in fig['layout']: fig['layout']['titlefont'] = dict()
            fig['layout']['titlefont']['size'] = getfontsize(width, binf=1000, bsup=2000, vinf=12, vsup=18)
            if 'annotations' in fig['layout']:
                for a in fig['layout']['annotations']:
                    a['font']['size'] = getfontsize(width, binf=1000, bsup=2000, vinf=10, vsup=14)
            if 'legend' not in fig['layout']: fig['layout']['legend'] = dict()
            if 'font' not in fig['layout']['legend']: fig['layout']['legend']['font'] = dict()
            fig['layout']['legend']['font']['size'] = getfontsize(width, binf=500, bsup=2000, vinf=8, vsup=12)
            fig['layout']['legend']['x'] = 1.02
            numleftyaxis = 0
            numrightyaxis = 0
            numxaxis = 0
            figtype = None

            for e in fig['data']:
                if e['type'] == 'pie': figtype = 'pie'
            for e in list(fig['layout']):
                if 'yaxis' in e:
                    if 'side' not in fig['layout'][e]: del fig['layout'][e]
                    else:
                        if fig['layout'][e]['side'] == 'left': numleftyaxis += 1
                        if fig['layout'][e]['side'] == 'right': numrightyaxis += 1
                if 'xaxis' in e: numxaxis += 1
            if figtype == 'pie':
                numleftyaxis = 0
                numrightyaxis = 0
                for e in list(fig['layout']):
                    if 'xaxis' in e or 'yaxis' in e: del fig['layout'][e]
            for e in fig['layout']:
                if 'yaxis' in e or 'xaxis' in e:
                    if 'titlefont' not in fig['layout'][e]: fig['layout'][e]['titlefont'] = dict()
                    if 'tickfont' not in fig['layout'][e]: fig['layout'][e]['tickfont'] = dict()
                    fig['layout'][e]['tickfont']['size'] = getfontsize(width, binf=500, bsup=2000, vinf=8, vsup=12)
                    fig['layout'][e]['titlefont']['size'] = getfontsize(width, binf=500, bsup=2000, vinf=10, vsup=14)
                if 'yaxis' in e:
                    fig['layout'][e]['position'] = getyposition(fig['layout'][e], width, numleftyaxis=numleftyaxis, rows=rows)
            for e in fig['layout']:
                if 'xaxis' in e:
                    if 'xaxis' == e: index = 0
                    else: index = int(e[-1]) - 1
                    fig['layout'][e]['domain'] = getdomain(width, index=index, numleftyaxis=numleftyaxis, numrightyaxis=numrightyaxis, numxaxis=numxaxis, rows=rows)
            if figtype == 'pie':
                index = 0
                for e in fig['data']:
                    if 'domain' not in e: e['domain'] = dict()
                    e['domain']['x'] = getdomain(width, index=index, numleftyaxis=numleftyaxis, numrightyaxis=numrightyaxis, numxaxis=numxaxis, rows=rows)
                    index += 1       
            if 'annotations' in fig['layout']:
                    index = 0
                    for a in list(fig['layout']['annotations']):
                        if plotorientation == 'horizontal': a['x'] = getaposition(width, index=index, numleftyaxis=numleftyaxis, numrightyaxis=numrightyaxis, numxaxis=numxaxis)
                        else: a['y'] = getaposition(width, index=index, numleftyaxis=numleftyaxis, numrightyaxis=numrightyaxis, numxaxis=numxaxis, rows=rows)
                        index += 1
            logging.debug('Generated figure: ' + json.dumps(chartobj))
        except:
            tb = sys.exc_info()
            message = str(tb[1])
            logging.error(message)
            status.error = message
        if status.error: return web.json_response(dict(success=False, message="Runchart function completed with errors!"))
        else: return web.json_response(dict(success=True, data=dict(chart=chartobj)))