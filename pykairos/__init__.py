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
import string, random, ssl, logging, os, subprocess, zipfile, re, json,  time, magic, cgi, sys, urllib, psycopg2, io, time
from pykairos.context import Context
from pykairos.analyzer import Analyzer
from datetime import datetime
from aiohttp import web, WSCloseCode, WSMsgType, MultiDict
from urllib.parse import parse_qs

logging.TRACE = 5
logging.addLevelName(5, "TRACE")
logging.trace = lambda m: logging.log(logging.TRACE, m)

global kairos
kairos=dict()

# Lambdas
getresponse = lambda context, d: web.json_response(dict(success=False, message=context.status.errormessages[0]) if context.status.errors > 0 else dict(success=True, **d))
        
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
        app.router.add_get('/clearprogenycaches', s.clearprogenycaches)
        app.router.add_get('/buildprogenycaches', s.buildprogenycaches)
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


                
    @intercept_logging_and_internal_error
    @trace_call
    def getid(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        pattern = params['pattern'][0]
        context = Context(nodesdb=nodesdb)
        result = context.expand(pattern, 'desc', 1, 0)
        context.free()
        return getresponse(context, dict(data=result))

    @intercept_logging_and_internal_error
    @trace_call
    def checkserverconfig(s, request):
        context = Context(postgres=True)
        context.createsystem()
        context.createuser('admin', skiperror=True)
        context.free()
        return getresponse(context, dict())

    @intercept_logging_and_internal_error
    @trace_call
    def createsystem(s, request):
        context = Context(postgres=True)
        context.createsystem()
        context.free()
        return getresponse(context, dict())

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
        context = Context(nodesdb=database)
        try:
            (id, typeobj) = context.writeobject(source)
            msg = dict(data=dict(msg='Object: ' + id + ' of type: ' + typeobj + ' has been successfully saved!'))
        except:
            tb = sys.exc_info()
            context.status.pusherrmessage(str(tb[1]))
        context.free()
        return getresponse(context, msg)


    @intercept_logging_and_internal_error
    @trace_call
    def getsettings(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        context = Context(nodesdb='kairos_user_' + user)
        settings = context.getsettings()
        context.free()
        return getresponse(context, dict(data=dict(settings=settings)))

    @intercept_logging_and_internal_error
    @trace_call
    def listdatabases(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        adminrights = True if params['admin'][0] == "true" else False
        context = Context(postgres=True)
        data = context.listdatabases(user, adminrights)
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listsystemdb(s, request):
        context = Context(postgres=True)
        data = context.listsystemdb()
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listnodesdb(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        context = Context(postgres=True)
        data = context.listnodesdb(user)
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listtemplates(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        try: context = Context(nodesdb=nodesdb, systemdb=systemdb)
        except: context = Context(systemdb=systemdb)
        data = context.listobjects("where type='template'")
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listaggregators(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        data = context.listobjects("where type='aggregator'")
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listliveobjects(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        data = context.listobjects("where type='liveobject'")
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listwallpapers(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]      
        try: context = Context(nodesdb=nodesdb, systemdb=systemdb)
        except: context = Context(systemdb=systemdb)
        data = context.listobjects("where type='wallpaper'")
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listcolors(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        try: context = Context(nodesdb=nodesdb, systemdb=systemdb)
        except: context = Context(systemdb=systemdb)
        data = context.listobjects("where type='color'")
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listobjects(s, request):
        params = parse_qs(request.query_string)
        systemdb = params['systemdb'][0]
        nodesdb = params['nodesdb'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        data = context.listobjects("")
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def getobject(s, request):
        params = parse_qs(request.query_string)
        database = params['database'][0]
        objtype = params['type'][0]
        objid = params['id'][0]
        context = Context(nodesdb=database)
        (_, source) = context.getobjectstream(objid, objtype)
        context.free()
        return getresponse(context, dict(data=source.decode()))

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
        top = int(params['top'][0])
        plotorientation = params['plotorientation'][0]
        logging = params['logging'][0]
        newsettings = dict(nodesdb=nodesdb, systemdb=systemdb, colors=colors, template=template, wallpaper=wallpaper, plotorientation=plotorientation, logging=logging, top=top)
        context = Context(nodesdb='kairos_user_' + user)
        context.updatesettings(newsettings)
        context.free()
        return getresponse(context, dict())

    @intercept_logging_and_internal_error
    @trace_call
    async def uploadobject(s, request):
        params = parse_qs(request.query_string)
        if 'mode' in params:
            mode = params['mode'][0]
            if mode == 'conf':
                return web.json_response(dict(success=True, maxFileSize=2147483648))
        multipart = await request.post()
        nodesdb = multipart['nodesdb'] if 'nodesdb' in multipart else params['nodesdb'][0]
        context = Context(nodesdb=nodesdb)
        (id, filename, typeobj) = context.uploadobject(multipart)
        context.free()
        return getresponse(context, dict(state=True, name=filename, id=id, type=typeobj))

    @intercept_logging_and_internal_error
    @trace_call
    async def uploadnode(s, request):
        params = parse_qs(request.query_string)
        if 'mode' in params:
            mode = params['mode'][0]
            if mode == 'conf':
                return web.json_response(dict(success=True, maxFileSize=2147483648))
        multipart = await request.post()
        nodesdb = multipart['nodesdb'] if 'nodesdb' in multipart else params['nodesdb'][0]
        systemdb = multipart['systemdb'] if 'systemdb' in multipart else params['systemdb'][0]
        id = multipart['id'] if 'id' in multipart else params['id'][0] if 'id' in params else None
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        filename = context.uploadnode(id, multipart)
        context.free()
        return getresponse(context, dict(state=True, name=filename))

    @intercept_logging_and_internal_error
    @trace_call
    def listroles(s, request):
        context = Context(postgres=True)
        data = context.listroles()
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listusers(s, request):
        context = Context(postgres=True)
        data = context.listusers()
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def listgrants(s, request):
        context = Context(postgres=True)
        data = context.listgrants()
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def createrole(s, request):
        params = parse_qs(request.query_string)
        role = params['role'][0]
        context = Context(postgres=True)
        response = context.createrole(role)
        context.free()
        return getresponse(context, response)

    @intercept_logging_and_internal_error
    @trace_call
    def createuser(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        context = Context(postgres=True)
        response = context.createuser(user)
        context.free()
        return getresponse(context, response)

    @intercept_logging_and_internal_error
    @trace_call
    def creategrant(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        role = params['role'][0]
        context = Context(postgres=True)
        response = context.creategrant(user, role)
        context.free()
        return getresponse(context, response)

    @intercept_logging_and_internal_error
    @trace_call
    def deleterole(s, request):
        params = parse_qs(request.query_string)
        role = params['role'][0]
        context = Context(postgres=True)
        response = context.deleterole(role)
        context.free()
        return getresponse(context, response)

    @intercept_logging_and_internal_error
    @trace_call
    def deleteuser(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        context = Context(postgres=True)
        response = context.deleteuser(user)
        context.free()
        return getresponse(context, response)

    @intercept_logging_and_internal_error
    @trace_call
    def resetpassword(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        context = Context(postgres=True)
        response = context.resetpassword(user)
        context.free()
        return getresponse(context, response)

    @intercept_logging_and_internal_error
    @trace_call
    def deletegrant(s, request):
        params = parse_qs(request.query_string)
        user = params['user'][0]
        role = params['role'][0]
        context = Context(postgres=True)
        response = context.deletegrant(user, role)
        context.free()
        return getresponse(context, response)

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
        context = Context(postgres=True)
        context.changepassword(user, new)
        context.free()
        return getresponse(context, dict(data=dict(msg='Password has been successfully updated!')))

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
        context = Context(nodesdb=database)
        context.deleteobject(id, typeobj)
        context.free()
        return getresponse(context, dict(data=dict(msg=id + ' ' + typeobj + ' object has been successfully removed!')))

    @intercept_logging_and_internal_error
    @trace_call
    def downloadobject(s, request):
        params = parse_qs(request.query_string)
        database = params['database'][0]
        id = params['id'][0]
        typeobj = params['type'][0]
        context = Context(nodesdb=database)
        (filename, stream) = context.getobjectstream(id, typeobj)
        context.free()
        return web.Response(headers=MultiDict({'Content-Disposition': 'Attachment;filename="' + filename + '"'}), body=stream)

    @intercept_logging_and_internal_error
    @trace_call
    def downloadsource(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb)
        (filename, stream) = context.downloadsource(id)
        context.free()
        return web.Response(headers=MultiDict({'Content-Disposition': 'Attachment;filename="' + filename + '"'}), body=stream)

    @intercept_logging_and_internal_error
    @trace_call
    def getBchildren(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb)
        data = context.getchildren(id)
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def getmemberlist(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb)
        node = context.getnode(id)
        context.getsource(node, getstream=True)
        context.free()
        thezip = zipfile.ZipFile(io.BytesIO(node['datasource']['stream']))
        data = [dict(label=x) for x in thezip.namelist()]
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def getcollections(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        data = context.getcollections(id)
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def getmember(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        member = params['member'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb)
        node = context.getnode(id)
        context.getsource(node, getstream=True)
        context.free()
        thezip = zipfile.ZipFile(io.BytesIO(node['datasource']['stream']))
        stream = thezip.read(member)
        type = magic.from_buffer(stream)
        stream = stream.decode().replace('#=', '# =').replace('#+', '# +')
        if 'html' in type.lower(): html = stream
        elif 'text' in type.lower(): html = '<pre>' + cgi.escape(stream) + '</pre>'
        else: html = 'Not yet taken into account'
        return getresponse(context, dict(data=html))

    @intercept_logging_and_internal_error
    @trace_call
    def getmenus(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        data = context.getmenus()
        context.free()
        return getresponse(context, dict(data=data))

    @intercept_logging_and_internal_error
    @trace_call
    def gettree(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        parent = params['id'][0]
        context = Context(nodesdb=nodesdb)
        result = context.gettree(parent)
        context.free
        return web.json_response(result)

    @intercept_logging_and_internal_error
    @trace_call
    def getnode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb)
        node = context.getnode(id)
        context.getsource(node)
        context.getcache(node)
        context.free()
        return getresponse(context, dict(data=node))

    @intercept_logging_and_internal_error
    @trace_call
    def createnode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb)
        child = context.createnode(id)
        node = context.getnode(child)
        context.free()
        return getresponse(context, dict(data=node))

    @intercept_logging_and_internal_error
    @trace_call
    def renamenode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        new = params['new'][0]
        context = Context(nodesdb=nodesdb)
        node = context.renamenode(id, new)
        context.free()
        return getresponse(context, dict(data=node))

    @intercept_logging_and_internal_error
    @trace_call
    def deletenode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb)
        context.deletenode(id)
        context.free()
        return getresponse(context, dict())

    @intercept_logging_and_internal_error
    @trace_call
    def emptytrash(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        context = Context(nodesdb=nodesdb)
        context.emptytrash()
        context.free()
        return getresponse(context, dict())

    @intercept_logging_and_internal_error
    @trace_call
    def movenode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        pfrom = params['from'][0]
        pto = params['to'][0]
        context = Context(nodesdb=nodesdb)
        node = context.movenode(pfrom, pto)
        context.free()
        return getresponse(context, dict(data=node))

    @intercept_logging_and_internal_error
    @trace_call
    def getchart(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        chart = params['chart'][0]
        variables = json.loads(params['variables'][0])
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        for v in variables: context.variables[v] = variables[v]
        chart = context.getchart(chart)
        context.free()
        return getresponse(context, dict(data=chart))

    @intercept_logging_and_internal_error
    @trace_call
    def getjsonobject(s, request):
        params = parse_qs(request.query_string)
        database = params['database'][0]
        id = params['id'][0]
        type = params['type'][0]
        context = Context(nodesdb=database, systemdb=database)
        obj = context.readobjects("where id = '" + str(id) + "' and type = '" + type + "'", evalobject=False)[0]
        context.free()
        return getresponse(context, dict(data=obj))
    
    @intercept_logging_and_internal_error
    @trace_call
    def getlayout(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        layout = params['layout'][0]
        variables = json.loads(params['variables'][0])
        context = Context(nodesdb=database, systemdb=database)
        for v in variables: context.variables[v] = variables[v]
        layout = context.getlayout(layout)
        context.free()
        return getresponse(context, dict(data=layout))
    
    @intercept_logging_and_internal_error
    @trace_call
    def getchoice(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        choice = params['choice'][0]
        variables = json.loads(params['variables'][0])
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        for v in variables: context.variables[v] = variables[v]
        choice = context.getchoice(choice)
        context.free()
        return getresponse(context, dict(data=choice))

    @intercept_logging_and_internal_error
    @trace_call
    def gettemplate(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        template = params['template'][0]
        context = Context(nodesdb=database, systemdb=database)
        template = context.gettemplate(template)
        context.free()
        return getresponse(context, dict(data=template))

    @intercept_logging_and_internal_error
    @trace_call
    def getcolors(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        colors = params['colors'][0]
        context = Context(nodesdb=database, systemdb=database)
        colors = context.getcolors(colors)
        context.free()
        return getresponse(context, dict(data=colors))

    @intercept_logging_and_internal_error
    @trace_call
    def getqueries(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        queries = context.listobjects("where type='query'")
        context.free()
        return getresponse(context, dict(data=queries))

    @intercept_logging_and_internal_error
    @trace_call
    def getcharts(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        charts = context.listobjects("where type='chart'")
        context.free()
        return getresponse(context, dict(data=charts))

    @intercept_logging_and_internal_error
    @trace_call
    def getchoices(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        choices = context.listobjects("where type='choice'")
        context.free()
        return getresponse(context, dict(data=choices))

    @intercept_logging_and_internal_error
    @trace_call
    def executequery(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        query = params['query'][0]
        limit = int(params['top'][0])
        variables = json.loads(params['variables'][0])
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        for v in variables: context.variables[v] = variables[v]
        result = context.executequery(id, query, limit)
        context.free()
        return getresponse(context, dict(data=result))

    @intercept_logging_and_internal_error
    @trace_call
    def displaycollection(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        collection = params['collection'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        result = context.displaycollection(id, collection)
        context.free()
        return getresponse(context, dict(data=result))

    @intercept_logging_and_internal_error
    @trace_call
    def buildcollectioncache(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        collection = params['collection'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        context.buildcollectioncache(id, {collection})
        context.free()
        return getresponse(context, dict())

    @intercept_logging_and_internal_error
    @trace_call
    def buildallcollectioncaches(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        node = context.getnode(id)
        context.buildcollectioncache(id, {'*'})
        context.free()
        return getresponse(context, dict())

    @intercept_logging_and_internal_error
    @trace_call
    def clearcollectioncache(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb)
        context.deletecache(id)
        context.free()
        return getresponse(context, dict())

    @intercept_logging_and_internal_error
    @trace_call
    def dropcollectioncache(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        id = params['id'][0] 
        collection = params['collection'][0]
        context = Context(nodesdb=nodesdb)
        context.dropcollectioncache(id, [collection])
        context.free()
        return getresponse(context, dict())

    @intercept_logging_and_internal_error
    @trace_call
    def compareaddnode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        fromid = int(params['from'][0])
        toid = int(params['to'][0])
        context = Context(nodesdb=nodesdb)
        tnode = context.compareaddnode(fromid, toid)
        context.free()
        return getresponse(context, dict(data=tnode))
    
    @intercept_logging_and_internal_error
    @trace_call
    def aggregateaddnode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        fromid = int(params['from'][0])
        toid = int(params['to'][0])
        context = Context(nodesdb=nodesdb)
        tnode = context.aggregateaddnode(fromid, toid)
        context.free()
        return getresponse(context, dict(data=tnode))
    
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
        context = Context(nodesdb=nodesdb)
        node = context.applyaggregator(id, aggregatorselector, aggregatortake, aggregatorskip, aggregatortimefilter, aggregatorsort, aggregatormethod)
        context.free()
        return getresponse(context, dict(data=node))
     
    @intercept_logging_and_internal_error
    @trace_call
    def unload(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        (filename, stream) = context.unload(id)
        context.free()
        return web.Response(headers=MultiDict({'Content-Disposition': 'Attachment;filename="' + filename + '"'}), body=stream)
    
    @intercept_logging_and_internal_error
    @trace_call
    def linkfathernode(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        fromid = int(params['from'][0])
        toid = int(params['to'][0])
        context = Context(nodesdb=nodesdb)
        tnode = context.linkfathernode(fromid, toid)
        context.free()
        return getresponse(context, dict(data=tnode))

    @intercept_logging_and_internal_error
    @trace_call
    def applyliveobject(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        loname = params['liveobject'][0]
        id = int(params['id'][0])
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        node= context.applyliveobject(id, loname)
        context.free()
        return getresponse(context, dict(data=node))

    @intercept_logging_and_internal_error
    @trace_call
    def exportdatabase(s, request):
        params = parse_qs(request.query_string)
        nodesdb = [params['nodesdb'][0]] if 'nodesdb' in params else []
        context = Context(postgres=True)
        context.exportdatabases(nodesdb)
        context.free()
        return getresponse(context, dict(data=dict(msg="Database(s): " + str(nodesdb) + " has(ve) been exported sucessfully!")))

    @intercept_logging_and_internal_error
    @trace_call
    def importdatabase(s, request):
        params = parse_qs(request.query_string)
        nodesdb = [params['nodesdb'][0]] if 'nodesdb' in params else []
        context = Context(postgres=True)
        context.importdatabases(nodesdb)
        context.free()
        return getresponse(context, dict(data=dict(msg="Database(s): " + str(nodesdb) + " has(ve) been imported sucessfully!")))

    @trace_call
    def clearprogenycaches(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        context.clearprogenycaches(id)
        context.free()
        return getresponse(context, dict(data=dict(msg="Caches have been cleared sucessfully!")))

    @trace_call
    def buildprogenycaches(s, request):
        params = parse_qs(request.query_string)
        nodesdb = params['nodesdb'][0]
        systemdb = params['systemdb'][0]
        id = params['id'][0]
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        context.buildprogenycaches(id)
        context.free()
        return getresponse(context, dict(data=dict(msg="Caches have been built sucessfully!")))

    @intercept_logging_and_internal_error
    @trace_call
    def runchart(s, request):
        params = parse_qs(request.query_string)
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
        context = Context(nodesdb=nodesdb, systemdb=systemdb)
        for v in variables: context.variables[v] = variables[v]
        chartobj = context.runchart(id, chart, width, height, limit, colors, plotorientation, template)
        context.free()
        return getresponse(context, dict(data=dict(chart=chartobj)))