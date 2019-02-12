class UserObject(dict):
    def __init__(s):
        object = {
            "type": "analyzer",
            "id": "ANALT10046",
            "begin": s.begin,
            "end": s.end,
            "rules": [
                {"action": s.flushparsing, "regexp": "^END OF STMT", "scope": "TPARSING"},

            ],
            "contextrules": [
                {"action": s.getrequest, "regexp": '^(.+)$', "context": "request", "scope": "TPARSING"},
                {"action": s.getbindnum, "regexp": '^ Bind#(\d+)$', "context": "bind", "scope": "TBINDS"},
                {"action": s.getbindtype, "regexp": '^  oacdty=(\d+) ', "context": "bindtype", "scope": "TBINDS"},
                {"action": s.getbindvalue, "regexp": '^  value=(.+)$', "context": "bindvalue", "scope": "TBINDS"},
            ],
            "outcontextrules": [
                {"action": s.getopid, "regexp": '^Oracle process number: (\d+)', "scope": "TPARSING"},
                {"action": s.getpid, "regexp": '^Unix process pid: (\d+), image: (.+?)$', "scope": "TPARSING"},
                {"action": s.getsid, "regexp": '^\*\*\* SESSION ID:\((.+?)\)', "scope": "TPARSING"},
                {"action": s.getclose, "regexp": '^CLOSE #(\d+):c=(\d+),e=(\d+),dep=(\d+),type=(\d+),tim=(\d+)$', "scope": "TCLOSE"},
                {"action": s.getparsing, "regexp": "^PARSING IN CURSOR #(\d+) len=(\d+) dep=(\d+) uid=(\d+) oct=(\d+) lid=(\d+) tim=(\d+) hv=(\d+) ad='(.+?)' sqlid='(.+?)'$", "scope": "TPARSING"},
                {"action": s.getexec, "regexp": "^EXEC #(\d+):c=(\d+),e=(\d+),p=(\d+),cr=(\d+),cu=(\d+),mis=(\d+),r=(\d+),dep=(\d+),og=(\d+),plh=(\d+),tim=(\d+)$", "scope": "TEXEC"},
                {"action": s.getfetch, "regexp": "^FETCH #(\d+):c=(\d+),e=(\d+),p=(\d+),cr=(\d+),cu=(\d+),mis=(\d+),r=(\d+),dep=(\d+),og=(\d+),plh=(\d+),tim=(\d+)$", "scope": "TFETCH"},
                {"action": s.getstat, "regexp": "^STAT #(\d+) id=(\d+) cnt=(\d+) pid=(\d+) pos=(\d+) obj=(\d+) op='(.+?) \(cr=(\d+) pr=(\d+) pw=(\d+) str=(\d+) time=(\d+) (\w+)", "scope": "TSTAT"},
                {"action": s.getwait, "regexp": "^WAIT #(\d+): nam='(.+?)' ela= (\d+) .+tim=(\d+)", "scope": "TWAIT"},
                {"action": s.geterror, "regexp": "^ERROR #(\d+):err=(\d+) tim=(\d+)", "scope": "TERROR"},
                {"action": s.getbinds, "regexp": "^BINDS #(\d+):", "scope": "TBINDS"},
                {"action": s.getxctend, "regexp": "^XCTEND rlb=(\d+), rd_only=(\d+), tim=(\d+)$", "scope": "TXCTEND"},
            ]
        }
        super(UserObject, s).__init__(**object)

    def begin(s, a):
        pass

    def end(s, a):
        pass
    
    def getopid(s, a, l, g, m):
        a.opid = int(g(1))
    
    def getpid(s, a, l, g, m):
        a.pid = int(g(1))
        a.image = g(2)
    
    def getsid(s, a, l, g, m):
        a.sid = g(1)

    def getclose(s, a, l, g, m):
        desc = dict(cid='text',c='bigint',e='bigint',dep='int',type='int',tim='bigint')
        cid = str(g(1))
        c = int(g(2))
        e = int(g(3))
        dep = int(g(4))
        type = int(g(5))
        tim = int(g(6))
        a.emit('TCLOSE', desc, dict(cid=cid,c=c,e=e,dep=dep,type=type,tim=tim))

    def getparsing(s, a, l, g, m):
        desc = dict(cid='text',opid='int',pid='int',image='text',sid='text',dep='int',uid='int',tim='bigint',hv='bigint',ad='text',sqlid='text',request='text')
        cid = str(g(1))
        dep = int(g(3))
        uid = int(g(4))
        tim = int(g(7))
        hv = int(g(8))
        ad = str(g(9))
        sqlid = str(g(10))
        a.desc = desc
        a.data = dict(cid=cid,opid=a.opid,pid=a.pid,image=a.image,sid=a.sid,dep=dep,uid=uid,tim=tim,hv=hv,ad=ad,sqlid=sqlid)
        a.count = 0
        a.setContext('request');

    def getrequest(s, a, l, g, m):
        a.request = a.request + str(g(1)) if a.count > 0 else ''
        a.count += 1

    def flushparsing(s, a, l, g, m):
        a.trace('DEBUG ANALT10046 request: ' +str(a.request))
        a.data['request'] = a.request
        a.emit('TPARSING', a.desc, a.data)
        a.setContext('');

    def getbinds(s, a, l, g, m):
        desc = dict(cid='text',id='int',type='text',value='text')
        cid = str(g(1))
        a.desc = desc
        a.data = dict(cid=cid)
        a.trace('DEBUG ANALT10046 cid: ' + cid)
        a.setContext('bind');

    def getbindnum(s, a, l, g, m):
        id = int(g(1))
        a.data['id'] = id
        a.trace('DEBUG ANALT10046 id: ' + str(id))
        a.setContext('bindtype');

    def getbindtype(s, a, l, g, m):
        type = str(g(1))
        a.data['type'] = type
        a.trace('DEBUG ANALT10046 type: ' + type)
        a.setContext('bindvalue');

    def getbindvalue(s, a, l, g, m):
        value = str(g(1))
        a.data['value'] = value
        a.trace('DEBUG ANALT10046 value: ' + value)
        a.emit('TBINDS', a.desc, a.data)
        a.setContext('');

    def getexec(s, a, l, g, m):
        desc = dict(cid='text',c='bigint',e='bigint',p='bigint',cr='bigint',cu='bigint',mis='int',r='bigint',dep='int',og='bigint',plh='bigint',tim='bigint')
        cid = str(g(1))
        c = int(g(2))
        e = int(g(3))
        p = int(g(4))
        cr = int(g(5))
        cu = int(g(6))
        mis = int(g(7))
        r = int(g(8))
        dep = int(g(9))
        og = int(g(10))
        plh = int(g(11))
        tim = int(g(12))
        a.emit('TEXEC', desc, dict(cid=cid,c=c,e=e,p=p,cr=cr,cu=cu,mis=mis,r=r,dep=dep,og=og,plh=plh,tim=tim))

    def getfetch(s, a, l, g, m):
        desc = dict(cid='text',c='bigint',e='bigint',p='bigint',cr='bigint',cu='bigint',mis='int',r='bigint',dep='int',og='bigint',plh='bigint',tim='bigint')
        cid = str(g(1))
        c = int(g(2))
        e = int(g(3))
        p = int(g(4))
        cr = int(g(5))
        cu = int(g(6))
        mis = int(g(7))
        r = int(g(8))
        dep = int(g(9))
        og = int(g(10))
        plh = int(g(11))
        tim = int(g(12))
        a.emit('TFETCH', desc, dict(cid=cid,c=c,e=e,p=p,cr=cr,cu=cu,mis=mis,r=r,dep=dep,og=og,plh=plh,tim=tim))

    def getstat(s, a, l, g, m):
        desc = dict(cid='text',id='int',cnt='int',pid='int',pos='int',obj='bigint',op='text',cr='bigint',pr='bigint',pw='bigint',st='int',time='bigint',unit='text')
        cid = str(g(1))
        id = int(g(2))
        cnt = int(g(3))
        pid = int(g(4))
        pos = int(g(5))
        obj = int(g(6))
        op = str(g(7))
        cr = int(g(8))
        pr = int(g(9))
        pw = int(g(10))
        st = int(g(11))
        time = int(g(12))
        unit = str(g(13))
        a.emit('TSTAT', desc, dict(cid=cid,id=id,cnt=cnt,pid=pid,pos=pos,obj=obj,op=op,cr=cr,pr=pr,pw=pw,st=st,time=time,unit=unit))

    def getwait(s, a, l, g, m):
        desc = dict(cid='text',nam='text',ela='bigint',tim='bigint')
        cid = str(g(1))
        nam = str(g(2))
        ela = int(g(3))
        tim = int(g(4))
        a.emit('TWAIT', desc, dict(cid=cid,nam=nam,ela=ela,tim=tim))

    def geterror(s, a, l, g, m):
        desc = dict(cid='text',err='int',tim='bigint')
        cid = str(g(1))
        err = int(g(2))
        tim = int(g(3))
        a.emit('TERROR', desc, dict(cid=cid,err=err,tim=tim))
        
    def getxctend(s, a, l, g, m):
        desc = dict(rlbk='int',rd_only='int',tim='bigint')
        rlbk = int(g(1))
        rd_only = int(g(2))
        tim = int(g(3))
        a.emit('TXCTEND', desc, dict(rlbk=rlbk,rd_only=rd_only,tim=tim))