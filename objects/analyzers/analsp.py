import re, logging
class UserObject(dict):
    def __init__(s):
        object = {
            "type": "analyzer",
            "id": "ANALSP",
            "begin": s.begin,
            "end": s.end,
            "rules": [
                {"action": s.askip, "regexp": '^(|Segments by|Foreground Wait|Service Wait)'},
                {"action": s.aend, "regexp": '^ +[\- ]+$'},
                {"action": s.afields, "regexp": '^-+[\- ]+$'},
                {"action": s.apat, "regexp": '^[a-zA-Z]+'}
            ],
            "contextrules": [
                {"action": s.aver, "regexp": '^.+\d+', "context": "ver"},
                {"action": s.atim, "regexp": 'End Snap: +\d+ (\d+)-([A-Z][a-z]+)-(\d+) (\d+):(\d+):(\d+) +(\S+)', "context": "tim"},
                {"action": s.axim, "regexp": ' +\d+ +\d+ +\d+-[A-Z][a-z]+-\d+ \d+:\d+:\d+ +(\d+)-([A-Z][a-z]+)-(\d+) (\d+):(\d+):(\d+) +(\S+)', "context": "xim"},
                {"action": s.adur, "regexp": 'Elapsed: +(\S+) +', "context": "dur"},
                {"action": s.asta, "regexp": '^.', "context": "sta", "scope": "DBORASTA"},
                {"action": s.adrv, "regexp": '^.', "context": "drv", "scope": "DBORADRV"},
                {"action": s.atms, "regexp": '^.', "context": "tms", "scope": "DBORATMS"},
                {"action": s.aweb, "regexp": '^.', "context": "web", "scope": "DBORAWEB"},
                {"action": s.awec, "regexp": '^.', "context": "wec", "scope": "DBORAWEC"},
                {"action": s.awev, "regexp": '^.', "context": "wev", "scope": "DBORAWEV"},
                {"action": s.alib, "regexp": '^.', "context": "lib", "scope": "DBORALIB"},
                {"action": s.alat, "regexp": '^.', "context": "lat", "scope": "DBORALAT"},
                {"action": s.alaw, "regexp": '^.', "context": "law", "scope": "DBORALAW"},
                {"action": s.amdc, "regexp": '^.', "context": "mdc", "scope": "DBORAMDC"},
                {"action": s.aenq, "regexp": '^.', "context": "enq", "scope": "DBORAENQ"},
                {"action": s.atbs, "regexp": '^.', "context": "tbs", "scope": "DBORATBS"},
                {"action": s.afil, "regexp": '^.', "context": "fil", "scope": "DBORAFIL"},
                {"action": s.asrv, "regexp": '^.', "context": "srv", "scope": "DBORASRV"},
                {"action": s.asvw, "regexp": '^.', "context": "svw", "scope": "DBORASVW"},
                {"action": s.arol, "regexp": '^.', "context": "rol", "scope": "DBORAROL"},
                {"action": s.asga, "regexp": '^.', "context": "sga", "scope": "DBORASGA"},
                {"action": s.apga, "regexp": '^E', "context": "pga", "scope": "DBORAPGA"},
                {"action": s.apgb, "regexp": '^ ', "context": "pgb", "scope": "DBORAPGB"},
                {"action": s.apgc, "regexp": '^.', "context": "pgc", "scope": "DBORAPGC"},
                {"action": s.aoss, "regexp": '^.', "context": "oss", "scope": "DBORAOSS"},
                {"action": s.abuf, "regexp": '^.', "context": "buf", "scope": "DBORABUF"},
                {"action": s.asglr, "regexp": '^.', "context": "sglr", "scope": "DBORASGLR"},
                {"action": s.asgpr, "regexp": '^.', "context": "sgpr", "scope": "DBORASGPR"},
                {"action": s.asgrlw, "regexp": '^.', "context": "sgrlw", "scope": "DBORASGRW"},
                {"action": s.asgcrbr, "regexp": '^.', "context": "sgcrbr", "scope": "DBORASGCRBR"},
                {"action": s.asgiw, "regexp": '^.', "context": "sgiw", "scope": "DBORASGIW"},
                {"action": s.asgbbw, "regexp": '^.', "context": "sgbbw", "scope": "DBORASGBBW"},
                {"action": s.asgfsc, "regexp": '^.', "context": "sgfsc", "scope": "DBORASGFSC"},
                {"action": s.asggcbb, "regexp": '^.', "context": "sggcbb", "scope": "DBORASGGCBB"},
                {"action": s.asgcbr, "regexp": '^.', "context": "sgcbr", "scope": "DBORASGCBR"},
                {"action": s.areq, "regexp": '^(.*)$', "context": "req"},
                {"action": s.amod, "regexp": '^Module: (.+)$|^(.+)$', "context": "mod"},
                {"action": s.asqc, "regexp": '^.', "context": "sqc", "scope": "DBORASQC"},
                {"action": s.asqe, "regexp": '^.', "context": "sqe", "scope": "DBORASQE"},
                {"action": s.asqg, "regexp": '^.', "context": "sqg", "scope": "DBORASQG"},
                {"action": s.asqrp, "regexp": '^.', "context": "sqrp", "scope": "DBORASQRP"},
                {"action": s.asqx, "regexp": '^.', "context": "sqx", "scope": "DBORASQX"},
                {"action": s.asqp, "regexp": '^.', "context": "sqp", "scope": "DBORASQP"},
                {"action": s.asqm, "regexp": '^.', "context": "sqm", "scope": "DBORASQM"},
                {"action": s.asqv, "regexp": '^.', "context": "sqv", "scope": "DBORASQV"},
                {"action": s.asqr, "regexp": '^.', "context": "sqr", "scope": "DBORASQR"},
                {"action": s.asqw, "regexp": '^.', "context": "sqw", "scope": "DBORASQW"},
                {"action": s.asqc, "regexp": '^.', "context": "sqc", "scope": "DBORAREQ"},
                {"action": s.asqe, "regexp": '^.', "context": "sqe", "scope": "DBORAREQ"},
                {"action": s.asqg, "regexp": '^.', "context": "sqg", "scope": "DBORAREQ"},
                {"action": s.asqrp, "regexp": '^.', "context": "sqrp", "scope": "DBORAREQ"},
                {"action": s.asqx, "regexp": '^.', "context": "sqx", "scope": "DBORAREQ"},
                {"action": s.asqp, "regexp": '^.', "context": "sqp", "scope": "DBORAREQ"},
                {"action": s.asqm, "regexp": '^.', "context": "sqm", "scope": "DBORAREQ"},
                {"action": s.asqv, "regexp": '^.', "context": "sqv", "scope": "DBORAREQ"},
                {"action": s.asqr, "regexp": '^.', "context": "sqr", "scope": "DBORAREQ"},
                {"action": s.asqw, "regexp": '^.', "context": "sqw", "scope": "DBORAREQ"},
                {"action": s.ahdr, "regexp": '^-+[- ]+$', "context": "hdr"},
            ],
            "xxx": [
                {"action": s.genstate('xim'), "regexp": 'Start Id +End Id +Start Time +'},
            ],
            "outcontextrules": [
                {"action": s.atype, "regexp": '(DB Name +DB Id +Instance +Inst Num Release +OPS Host)|(DB Name +DB Id +Instance +Inst Num Release +Cluster Host)|(Database +DB Id +Instance +Inst Num +Startup Time +Release +RAC)|(DB Name +DB Id +Instance +Inst Num Release +RAC Host)|(DB Name +DB Id +Instance +Inst Num Startup Time +Release +RAC)'},
                {"action": s.genstate('tim'), "regexp": 'Begin Snap: ' },
                {"action": s.genstate('tms'), "regexp": 'Time Model (System Stats|Statistics) +(for DB| DB\/Inst):', "scope": "DBORATMS"},
                {"action": s.genstate('wev'), "regexp": 'Foreground Wait Events +(for DB| DB\/Inst):', "scope": "DBORAWEV"},
                {"action": s.genstate('web'), "regexp": 'Background Wait Events +(for DB| DB/Inst):', "scope": "DBORAWEB"},
                {"action": s.genstate1('sqc'), "regexp": 'SQL ordered by CPU( Time| time| ) *(for DB| DB/Inst):', "scope": "DBORASQC"},
                {"action": s.genstate1('sqe'), "regexp": 'SQL ordered by Elapsed( Time| time| ) *(for DB| DB/Inst):', "scope": "DBORASQE"},
                {"action": s.genstate1('sqg'), "regexp": 'SQL ordered by Gets +(for DB| DB/Inst):', "scope": "DBORASQG"},
                {"action": s.genstate1('sqr'), "regexp": 'SQL ordered by Reads +(for DB| DB/Inst):', "scope": "DBORASQR"},
                {"action": s.genstate1('sqx'), "regexp": 'SQL ordered by Executions +(for DB| DB/Inst):', "scope": "DBORASQX"},
                {"action": s.genstate1('sqp'), "regexp": 'SQL ordered by Parse Calls +(for DB| DB/Inst):', "scope": "DBORASQP"},
                {"action": s.genstate1('sqm'), "regexp": 'SQL ordered by Sharable Memory +(for DB| DB/Inst):', "scope": "DBORASQM"},
                {"action": s.genstate1('sqv'), "regexp": 'SQL ordered by Version Count +(for DB| DB/Inst):', "scope": "DBORASQV"},
                {"action": s.genstate1('sqw'), "regexp": 'SQL ordered by Cluster Wait Time +(for DB| DB/Inst):', "scope": "DBORASQW"},
                {"action": s.genstate('sta'), "regexp": 'Instance Activity Stats +(for DB| DB\/Inst):', "scope": "DBORASTA"},
                {"action": s.genstate('drv'), "regexp": 'Statistics identified by ..derived.. come from sources other', "scope": "DBORADRV"},
                {"action": s.genstate('oss'), "regexp": '(O|Operating )(S|System) Statistics +(for DB| DB/Inst):', "scope": "DBORAOSS"},
                {"action": s.genstate('tbs'), "regexp": 'Tablespace IO Stats +(for DB| DB/Inst):', "scope": "DBORATBS"},
                {"action": s.genstate('fil'), "regexp": 'File IO Stats +(for DB| DB/Inst):', "scope": "DBORAFIL"},
                {"action": s.genstate('mdc'), "regexp": 'Memory Dynamic Components +(for DB| DB/Inst):', "scope": "DBORAMDC"},
                {"action": s.genstate('buf'), "regexp": 'Buffer Pool Statistics +(for DB| DB/Inst):', "scope": "DBORABUF"},
                {"action": s.genstate('enq'), "regexp": 'Enqueue (a|A)ctivity +(for DB| DB/Inst):', "scope": "DBORAENQ"},
                {"action": s.genstate('law'), "regexp": 'Latch Activity +(for DB| DB/Inst):', "scope": "DBORALAW"},
                {"action": s.genstate('lat'), "regexp": 'Latch Sleep (b|B)reakdown +(for DB| DB/Inst):', "scope": "DBORALAT"},
                {"action": s.genstate('lib'), "regexp": 'Library Cache Activity +(for DB| DB/Inst):', "scope": "DBORALIB"},
                {"action": s.genstate('sga'), "regexp": 'SGA breakdown difference +(for DB| DB/Inst):', "scope": "DBORASGA"},
                
                {"action": s.genstate('wec'), "regexp": 'Wait Class +(for DB| DB\/Inst):', "scope": "DBORAWEC"},
                {"action": s.genstate('srv'), "regexp": 'Service Statistics +(for DB| DB/Inst):', "scope": "DBORASRV"},
                {"action": s.genstate('svw'), "regexp": 'Service Wait Class Stats +(for DB| DB/Inst):', "scope": "DBORASVW"},
                {"action": s.genstate('rol'), "regexp": 'Rollback Segment Stats +(for DB| DB/Inst):', "scope": "DBORAROL"},
                {"action": s.genstate('pga'), "regexp": 'PGA Aggr Target Stats +(for DB| DB/Inst):', "scope": "DBORAPGA"},
                {"action": s.genstate('pgb'), "regexp": 'PGA Aggr Summary +(for DB| DB/Inst):', "scope": "DBORAPGB"},
                {"action": s.genstate('pgc'), "regexp": 'PGA Aggr Target Histogram +(for DB| DB/Inst):', "scope": "DBORAPGC"},
                {"action": s.genstate('sglr'), "regexp": 'Segments by Logical Reads +(for DB| DB/Inst):', "scope": "DBORASGLR"},
                {"action": s.genstate('sgpr'), "regexp": 'Segments by Physical Reads +(for DB| DB/Inst):', "scope": "DBORASGPR"},
                {"action": s.genstate('sgrlw'), "regexp": 'Segments by Row Lock Waits +(for DB| DB/Inst):', "scope": "DBORASGRLW"},
                {"action": s.genstate('sgcrbr'), "regexp": 'Segments by CR Blocks Received +(for DB| DB/Inst):', "scope": "DBORASGCRBR"},
                {"action": s.genstate('sgiw'), "regexp": 'Segments by ITL Waits +(for DB| DB/Inst):', "scope": "DBORASGIW"},
                {"action": s.genstate('sgbbw'), "regexp": 'Segments by Buffer Busy Waits +(for DB| DB/Inst):', "scope": "DBORASGBBW"},
                {"action": s.genstate('sggcbb'), "regexp": 'Segments by Global Cache Buffer Busy +(for DB|DB/Inst):', "scope": "DBORASGGCBB"},
                {"action": s.genstate('sgcbr'), "regexp": 'Segments by Current Blocks Received +(for DB| DB/Inst):', "scope": "DBORASGCBR"},
                {"action": s.genstate('sgfsc'), "regexp": 'Segments by Table Scans +(for DB| DB/Inst):', "scope": "DBORASGFSC"},
                {"action": s.genstate('sglr'), "regexp": 'Top \d+ Logical Reads per Segment +(for DB| DB/Inst):', "scope": "DBORASGLR"},
                {"action": s.genstate('sgpr'), "regexp": 'Top \d+ Pysical Reads per Segment +(for DB| DB/Inst):', "scope": "DBORASGPR"},
                {"action": s.genstate('sgbbw'), "regexp": 'Top \d+ Buf. Busy Waits per Segment +(for DB| DB/Inst):', "scope": "DBORASGBBW"},
                {"action": s.genstate('sgrlw'), "regexp": 'Top \d+ Row Lock Waits per Segment +(for DB| DB/Inst):', "scope": "DBORASGRLW"},
            ]
        }
        super(UserObject, s).__init__(**object)

    def begin(s, a):
        a.fields = []
        a.module = ''
        a.type = 'STATSPACK_8I'
        a.version = ''
        a.startup = ''
        a.state = ''
        a.tof=lambda x: float(x.replace(',','').replace('N/A','0').replace('#','9'))
        a.getstring=lambda f,x: x[a.fields[f][0]:a.fields[f][1]].rstrip()
        a.month=dict(Jan='01',Feb='02',Fev='02',Mar='03',Apr='04',Avr='04',May='05',Mai='05', Jun='06',Jul='07',Aug='08',Sep='09',Oct='10',Nov='11',Dec='12')
        a.getfloat=lambda f,x: a.tof(re.search('(^[-+]?[0-9,]*\.?[0-9]+([eE][-+]?[0-9]+)?$|^N/A$|^#+$)',x[a.fields[f][0]:a.fields[f][1]].lstrip().rstrip()).group(1))
        a.setContext('');

    def end(s, a):
        pass

    def aend(s, a, l ,g, m):
        a.fields = []
        if len(a.scope) < 3:
            if a.scope.issubset({'DBORAWEV'}) and a.context == 'wev': a.setContext('BREAK')
            if a.scope.issubset({'DBORAWEC'}) and a.context == 'wec': a.setContext('BREAK')
            if a.scope.issubset({'DBORAWEB'}) and a.context == 'web': a.setContext('BREAK')
            if a.scope.issubset({'DBORASTA'}) and a.context == 'sta': a.setContext('BREAK')
            if a.scope.issubset({'DBORADRV'}) and a.context == 'drv': a.setContext('BREAK')
            if a.scope.issubset({'DBORATMS'}) and a.context == 'tms': a.setContext('BREAK')
            if a.scope.issubset({'DBORAOSS'}) and a.context == 'oss': a.setContext('BREAK')
            if a.scope.issubset({'DBORASRV'}) and a.context == 'srv': a.setContext('BREAK')
            if a.scope.issubset({'DBORASVW'}) and a.context == 'svw': a.setContext('BREAK')
            if a.scope.issubset({'DBORALIB'}) and a.context == 'lib': a.setContext('BREAK')
            if a.scope.issubset({'DBORALAT'}) and a.context == 'lat': a.setContext('BREAK')
            if a.scope.issubset({'DBORALAW'}) and a.context == 'law': a.setContext('BREAK')
            if a.scope.issubset({'DBORAMDC'}) and a.context == 'mdc': a.setContext('BREAK')
            if a.scope.issubset({'DBORAENQ'}) and a.context == 'enq': a.setContext('BREAK')
            if a.scope.issubset({'DBORATBS'}) and a.context == 'tbs': a.setContext('BREAK')
            if a.scope.issubset({'DBORAFIL'}) and a.context == 'fil': a.setContext('BREAK')
            if a.scope.issubset({'DBORAROL'}) and a.context == 'rol': a.setContext('BREAK')
            if a.scope.issubset({'DBORASGA'}) and a.context == 'sga': a.setContext('BREAK')
            if a.scope.issubset({'DBORAPGA'}) and a.context == 'pga': a.setContext('BREAK')
            if a.scope.issubset({'DBORAPGB'}) and a.context == 'pgb': a.setContext('BREAK')
            if a.scope.issubset({'DBORAPGC'}) and a.context == 'pgc': a.setContext('BREAK')
            if a.scope.issubset({'DBORABUF'}) and a.context == 'buf': a.setContext('BREAK')
            if a.scope.issubset({'DBORASGLR'}) and a.context == 'sglr': a.setContext('BREAK')
            if a.scope.issubset({'DBORASGPR'}) and a.context == 'sgpr': a.setContext('BREAK')
            if a.scope.issubset({'DBORASGRLW'}) and a.context == 'sgrlw': a.setContext('BREAK')
            if a.scope.issubset({'DBORASGCRBR'}) and a.context == 'sgcrbr': a.setContext('BREAK')
            if a.scope.issubset({'DBORASGIW'}) and a.context == 'sgiw': a.setContext('BREAK')
            if a.scope.issubset({'DBORASGBBW'}) and a.context == 'sgbbw': a.setContext('BREAK')
            if a.scope.issubset({'DBORASGGCBB'}) and a.context == 'sggcbb': a.setContext('BREAK')
            if a.scope.issubset({'DBORASGCBR'}) and a.context == 'sgcbr': a.setContext('BREAK')
            if a.scope.issubset({'DBORASGFSC'}) and a.context == 'sgfsc': a.setContext('BREAK')
            if a.scope.issubset({'DBORASQC'}) and a.context == 'sqc': a.setContext('BREAK')
            if a.scope.issubset({'DBORASQE'}) and a.context == 'sqe': a.setContext('BREAK')
            if a.scope.issubset({'DBORASQG'}) and a.context == 'sqg': a.setContext('BREAK')
            if a.scope.issubset({'DBORASQR'}) and a.context == 'sqr': a.setContext('BREAK')
            if a.scope.issubset({'DBORASQRP'}) and a.context == 'sqrp': a.setContext('BREAK')
            if a.scope.issubset({'DBORASQX'}) and a.context == 'sqx': a.setContext('BREAK')
            if a.scope.issubset({'DBORASQP'}) and a.context == 'sqp': a.setContext('BREAK')
            if a.scope.issubset({'DBORASQW'}) and a.context == 'sqw': a.setContext('BREAK')
            if a.scope.issubset({'DBORASQM'}) and a.context == 'sqm': a.setContext('BREAK')
            if a.scope.issubset({'DBORASQV'}) and a.context == 'sqv': a.setContext('BREAK')
        if a.context != 'BREAK': a.setContext('')

    def genstate(s, c):
        def f(a, l ,g, m):
            a.setContext(c)
        return f

    def genstate1(s, c):
        def f(a, l, g, m):
            a.oldstate = a.state
            a.startstate = c
            a.setContext('hdr')
        return f

    def askip(s, a, l, g, m):
        a.fields = []

    def afields(s, a, l, g, m):
        pos=0
        for f in re.split('(-+)',l):
            if f and f[0]=='-': a.fields.append((pos,pos+len(f)))
            pos+=len(f)

    def apat(s, a, l, g, m):
        try: a.pattern=a.getstring(0,l)
        except: a.pattern=None
        try: a.pattern2=a.getstring(1,l)
        except: a.pattern2=None

    def atype(s, a, l, g, m):
        if g(1): a.type='STATSPACK_8I'
        if g(2): a.type='STATSPACK_9I'
        if g(3): a.type='STATSPACK_10G'
        if g(4): a.type='AWR_10G'
        if g(5): a.type='AWR_11G'
        a.setContext('ver')

    def aver(s, a, l, g, m):
        if a.type=='AWR_10G': a.version=a.getstring(4,l)
        if a.type=='AWR_11G':
            a.version=a.getstring(5,l)
            a.startup=a.getstring(4,l)
        a.setContext('')

    def amod(s, a, l, g, m):
        if g(1): a.module=g(1)
        if g(2): a.request+=g(2)
        a.setContext('req')
        a.state='req'

    def ahdr(s, a, l, g, m):
        if a.oldstate=='mod': a.setContext('mod')
        elif a.oldstate=='req': a.setContext('req')
        else: a.setContext(a.startstate)

    def axim(s, a, l, g, m):
        a.date='20'+g(3)+a.month[g(2)]+g(1)+g(4)+g(5)+g(6)+'000'
        a.dur=a.tof(g(7))*60
        if 'DBORAMISC' in a.scope:
            d=dict(timestamp='text',type='text',sessions='real',avgelapsed='real',elapsed='int')
            v=dict(timestamp=a.date,type=a.type,sessions=a.sessions,avgelapsed=a.dur,elapsed=int(a.dur))
            a.emit('DBORAMISC', d, v)
            if a.scope.issubset({'DBORAMISC'}): a.setContext('BREAK')
        if 'DBORAINFO' in a.scope:
            d=dict(timestamp='text',startup='text')
            v=dict(timestamp=a.date,startup=a.startup)
            a.emit('DBORAINFO', d, v)
            if a.scope.issubset({'DBORAINFO'}): a.setContext('BREAK')

    def adur(s, a, l, g, m):
        a.dur=a.tof(g(1))*60
        if 'DBORAMISC' in a.scope:
            d=dict(timestamp='text',type='text',sessions='real',avgelapsed='real',elapsed='int')
            v=dict(timestamp=a.date,type=a.type,sessions=a.sessions,avgelapsed=a.dur,elapsed=int(a.dur))
            a.emit('DBORAMISC', d, v)
            if a.scope.issubset({'DBORAMISC'}): a.setContext('BREAK')
        if 'DBORAINFO' in a.scope:
            d=dict(timestamp='text',startup='text')
            v=dict(timestamp=a.date,startup=a.startup)
            a.emit('DBORAINFO', d, v)
            if a.scope.issubset({'DBORAINFO'}): a.setContext('BREAK')

    def atim(s, a, l, g, m):
        a.date='20'+g(3)+a.month[g(2)]+g(1)+g(4)+g(5)+g(6)+'000'
        a.sessions=a.tof(g(7))
        a.setContext('dur')

    def asta(s, a, l, g, m):
        try:
            name=a.getstring(0,l)
            value=a.getfloat(1,l)/a.dur
        except: return
        d=dict(timestamp='text',statistic='text',value='real')
        v=dict(timestamp=a.date,statistic=name,value=value)
        a.emit('DBORASTA', d, v)

    def adrv(s, a, l, g, m):
        try:
            statistic=a.getstring(0,l)
            value=a.getfloat(1,l)/a.dur
        except: return
        d=dict(timestamp='text',statistic='text',value='real')
        v=dict(timestamp=a.date,statistic=statistic,value=value)
        a.emit('DBORADRV', d, v)

    def atms(s, a, l, g, m):
        try:
            statistic=a.getstring(0,l)
            time=a.getfloat(1,l)/a.dur
        except: return
        d=dict(timestamp='text',statistic='text',time='real')
        v=dict(timestamp=a.date,statistic=statistic,time=time)
        a.emit('DBORATMS', d, v)

    def awec(s, a, l, g, m):
        try:
            eclass=a.getstring(0,l)
            try:
                count=a.getfloat(1,l)/a.dur
                if '10G' in a.type or 'AWR' in a.type: timeouts=a.getfloat(2,l)*count/100
                else: timeouts=a.getfloat(2,l)/a.dur
            except:
                count=0
                timeouts=0
            time=a.getfloat(3,l)/a.dur
        except: return
        if a.type=='STATSPACK_8I': time=time/100
        d=dict(timestamp='text',eclass='text',count='real',timeouts='real',time='real')
        v=dict(timestamp=a.date,eclass=eclass,count=count,timeouts=timeouts,time=time)
        a.emit('DBORAWEC', d, v)

    def awev(s, a, l, g, m):
        try:
            event=a.getstring(0,l)
            count=a.getfloat(1,l)/a.dur
            if '10G' in a.type or 'AWR' in a.type: timeouts=a.getfloat(2,l)*count/100
            else: timeouts=a.getfloat(2,l)/a.dur
            time=a.getfloat(3,l)/a.dur
        except: return
        if a.type=='STATSPACK_8I': time=time/100
        d=dict(timestamp='text',event='text',count='real',timeouts='real',time='real')
        v=dict(timestamp=a.date,event=event,count=count,timeouts=timeouts,time=time)
        a.emit('DBORAWEV', d, v)

    def aweb(s, a, l, g, m):
        try:
            event=a.getstring(0,l)
            count=a.getfloat(1,l)/a.dur
            if '10G' in a.type or 'AWR' in a.type: timeouts=a.getfloat(2,l)*count/100
            else: timeouts=a.getfloat(2,l)/a.dur
            time=a.getfloat(3,l)/a.dur
        except: return
        if a.type=='STATSPACK_8I': time=time/100
        d=dict(timestamp='text',event='text',count='real',timeouts='real',time='real')
        v=dict(timestamp=a.date,event=event,count=count,timeouts=timeouts,time=time)
        a.emit('DBORAWEB', d, v)

    def areq(s, a, l, g, m):
        if g(1): a.request+=g(1)
        else:
            try:
                d=dict(sqlid='text',module='text',request='text')
                if 'setreq' not in a.common: a.common['setreq']=set()
                if a.sqlid not in a.common['setreq']:
                    a.common['setreq'].add(a.sqlid)
                    v=dict(sqlid=a.sqlid,module=a.module,request=a.request)
                    a.emit('DBORAREQ', d, v)
            except: pass
            a.state=a.startstate
            a.setContext(a.startstate)

    def alib(s, a, l, g, m):
        try:
            item=a.getstring(0,l)
            gets=a.getfloat(1,l)/a.dur
            pins=a.getfloat(3,l)/a.dur
            reloads=a.getfloat(5,l)/a.dur
            invalidations=a.getfloat(6,l)/a.dur
        except: return
        d=dict(timestamp='text',item='text',gets='real',pins='real',reloads='real',invalidations='real')
        v=dict(timestamp=a.date,item=item,gets=gets,pins=pins,reloads=reloads,invalidations=invalidations)
        a.emit('DBORALIB', d, v)

    def alat(s, a, l, g, m):
        try:
            gets=a.getfloat(1,l)/a.dur
            misses=a.getfloat(2,l)/a.dur
            sleeps=a.getfloat(3,l)/a.dur
        except: return
        latch=a.pattern
        d=dict(timestamp='text',latch='text',gets='real',misses='real',sleeps='real')
        v=dict(timestamp=a.date,latch=latch,gets=gets,misses=misses,sleeps=sleeps)
        a.emit('DBORALAT', d, v)

    def alaw(s, a, l, g, m):
        try:
            latch=a.getstring(0,l)
            wait=a.getfloat(4,l)/a.dur
        except: return
        d=dict(timestamp='text',latch='text',wait='real')
        v=dict(timestamp=a.date,latch=latch,wait=wait)
        a.emit('DBORALAW', d, v)

    def amdc(s, a, l, g, m):
        try:
            component=a.getstring(0,l)
            size=a.getfloat(2,l)
            vmin=a.getfloat(3,l)
            vmax=a.getfloat(4,l)
            opcount=a.getfloat(5,l)/a.dur
            operation=a.getstring(6,l)
        except: return
        d=dict(timestamp='text',component='text',operation='text',size='real',vmin='real',vmax='real',opcount='real')
        v=dict(timestamp=a.date,component=component,operation=operation,size=size,vmin=vmin,vmax=vmax,opcount=opcount)
        a.emit('DBORAMDC', d, v)

    def aenq(s, a, l, g, m):
        try:
            requests=a.getfloat(1,l)/a.dur
            succgets=a.getfloat(2,l)/a.dur
            failedgets=a.getfloat(3,l)/a.dur
            waits=a.getfloat(4,l)/a.dur
            avgwaitpersec=a.getfloat(6,l)*waits
        except: return
        enqueue=a.pattern
        d=dict(timestamp='text',enqueue='text',requests='real',succgets='real',failedgets='real',waits='real',avgwaitpersec='real')
        v=dict(timestamp=a.date,enqueue=enqueue,requests=requests,succgets=succgets,failedgets=failedgets,waits=waits,avgwaitpersec=avgwaitpersec)
        a.emit('DBORAENQ', d, v)

    def atbs(s, a, l, g, m):
        try:
            reads=a.getfloat(1,l)/a.dur
            readtime=a.getfloat(3,l)
            blocksperread=a.getfloat(4,l)
            writes=a.getfloat(5,l)/a.dur
            busy=a.getfloat(7,l)/a.dur
            busytime=a.getfloat(8,l)
        except: return
        tablespace=a.pattern
        d=dict(timestamp='text',tablespace='text',reads='real',readtime='real',blocksperread='real',writes='real',busy='real',busytime='real')
        v=dict(timestamp=a.date,tablespace=tablespace,reads=reads,readtime=readtime,blocksperread=blocksperread,writes=writes,busy=busy,busytime=busytime)
        a.emit('DBORATBS', d, v)

    def afil(s, a, l, g, m):
    #if not 'AWR' in a.type: return
        try:
            reads=a.getfloat(2,l)/a.dur
            readtime=a.getfloat(4,l)
            blocksperread=a.getfloat(5,l)
            writes=a.getfloat(6,l)/a.dur
            busy=a.getfloat(8,l)/a.dur
            busytime=a.getfloat(9,l)
        except: return
        tablespace=a.pattern
        file=a.pattern2
        d=dict(timestamp='text',tablespace='text',file='text',reads='real',readtime='real',blocksperread='real',writes='real',busy='real',busytime='real')
        v=dict(timestamp=a.date,tablespace=tablespace,file=file,reads=reads,readtime=readtime,blocksperread=blocksperread,writes=writes,busy=busy,busytime=busytime)
        a.emit('DBORAFIL', d, v)

    def arol(s, a, l, g, m):
        try:
            segment=a.getstring(0,l)
            gets=a.getfloat(1,l)/a.dur
            bytes=a.getfloat(3,l)/a.dur
            wraps=a.getfloat(4,l)/a.dur
            shrinks=a.getfloat(5,l)/a.dur
            extends=a.getfloat(6,l)/a.dur
        except: return
        d=dict(timestamp='text',segment='text',gets='real',bytes='real',wraps='real',shrinks='real',extends='real')
        v=dict(timestamp=a.date,segment=segment,gets=gets,bytes=bytes,wraps=wraps,shrinks=shrinks,extends=extends)
        a.emit('DBORAROL', d, v)

    def asga(s, a, l, g, m):
        try:
            pool=a.getstring(0,l)
            name=a.getstring(1,l)
            size=a.getfloat(3,l)
        except: return
        if a.type not in ['STATSPACK_10G','AWR_10G','AWR_11G'] : size=size/(1024*1024)
        d=dict(timestamp='text',pool='text',name='text',size='real')
        v=dict(timestamp=a.date,pool=pool,name=name,size=size)
        a.emit('DBORASGA', d, v)

    def apga(s, a, l, g, m):
        if 'AWR' in a.type:
            try:
                aggrtarget=a.getfloat(1,l)
                autotarget=a.getfloat(2,l)
                memalloc=a.getfloat(3,l)
                memused=a.getfloat(4,l)
            except: return
        else:
            try:
                aggrtarget=a.getfloat(4,l)
                autotarget=a.getfloat(5,l)
                memalloc=a.getfloat(6,l)
                memused=a.getfloat(7,l)
            except: return
        d=dict(timestamp='text',aggrtarget='real',autotarget='real',memalloc='real',memused='real')
        v=dict(timestamp=a.date,aggrtarget=aggrtarget,autotarget=autotarget,memalloc=memalloc,memused=memused)
        a.emit('DBORAPGA', d, v)

    def apgb(s, a, l, g, m):
        try:
            pgahit=a.getfloat(0,l)
            wamemory=a.getfloat(1,l)/a.dur
            extramemory=a.getfloat(2,l)/a.dur
        except: return
        d=dict(timestamp='text',pgahit='real',wamemory='real',extramemory='real')
        v=dict(timestamp=a.date,pgahit=pgahit,wamemory=wamemory,extramemory=extramemory)
        a.emit('DBORAPGB', d, v)

    def apgc(s, a, l, g, m):
        try:
            highoptimal=a.getstring(1,l)
            totexecs=a.getfloat(2,l)/a.dur
            execs0=a.getfloat(3,l)/a.dur
            execs1=a.getfloat(4,l)/a.dur
            execs2=a.getfloat(5,l)/a.dur
        except: return
        d=dict(timestamp='text',highoptimal='text',totexecs='real',execs0='real',execs1='real',execs2='real')
        v=dict(timestamp=a.date,highoptimal=highoptimal,totexecs=totexecs,execs0=execs0,execs1=execs1,execs2=execs2)
        a.emit('DBORAPGC', d, v)

    def asqc(s, a, l, g, m):
        if 'AWR' in a.type:
            try:
                cpu=a.getfloat(0,l)/a.dur
                elapsed=a.getfloat(4,l)/a.dur if '11.2' in a.version  or '12.1' in a.version else a.getfloat(1,l)/a.dur
                execs=a.getfloat(1,l)/a.dur if '11.2' in a.version  or '12.1' in a.version else a.getfloat(2,l)/a.dur
                percent=a.getfloat(3,l) if '11.2' in a.version  or '12.1' in a.version else a.getfloat(4,l)
                gets=0.0
                a.sqlid=a.getstring(5,l).lstrip() if 'AWR_10G' in a.type else a.getstring(6,l).lstrip()
                a.sqlid=a.getstring(6,l).lstrip() if '10.2.0.5' in a.version else a.sqlid
                a.sqlid=a.getstring(7,l).lstrip() if '11.2' in a.version  or '12.1' in a.version else a.sqlid
            except: return
        else:
            try:
                cpu=a.getfloat(0,l)/a.dur
                execs=a.getfloat(1,l)/a.dur
                percent=a.getfloat(3,l)
                elapsed=a.getfloat(4,l)/a.dur
                gets=a.getfloat(5,l)/a.dur
                a.sqlid=a.getstring(6,l).lstrip()
            except: return
        d=dict(timestamp='text',sqlid='text',gets='real',execs='real',cpu='real',elapsed='real',percent='real')
        v=dict(timestamp=a.date,sqlid=a.sqlid,gets=gets,execs=execs,cpu=cpu,elapsed=elapsed,percent=percent)
        if 'DBORASQC' in a.scope: a.emit('DBORASQC', d, v)
        a.state='mod'
        a.setContext('mod')
        a.request=''

    def asqe(s, a, l, g, m):
        if 'AWR' in a.type:
            try:
                elapsed=a.getfloat(0,l)/a.dur
                cpu=elapsed*a.getfloat(4,l)/100 if '11.2' in a.version  or '12.1' in a.version else a.getfloat(1,l)/a.dur
                execs=a.getfloat(1,l)/a.dur if '11.2' in a.version  or '12.1' in a.version else a.getfloat(2,l)/a.dur
                percent=a.getfloat(3,l) if '11.2' in a.version  or '12.1' in a.version else a.getfloat(4,l)
                reads=0.0
                a.sqlid=a.getstring(5,l).lstrip()
                a.sqlid=a.getstring(6,l).lstrip() if '11.2' in a.version  or '12.1' in a.version else a.sqlid
            except: return
        else:
            try:
                elapsed=a.getfloat(0,l)/a.dur
                execs=a.getfloat(1,l)/a.dur
                percent=a.getfloat(3,l)
                cpu=a.getfloat(4,l)/a.dur
                reads=a.getfloat(5,l)/a.dur
                a.sqlid=a.getstring(6,l).lstrip()
            except: return
        d=dict(timestamp='text',sqlid='text',reads='real',execs='real',cpu='real',elapsed='real',percent='real')
        v=dict(timestamp=a.date,sqlid=a.sqlid,reads=reads,execs=execs,cpu=cpu,elapsed=elapsed,percent=percent)
        if 'DBORASQE' in a.scope: a.emit('DBORASQE', d, v)
        a.state='mod'
        a.setContext('mod')
        a.request=''

    def asqp(s, a, l, g, m):
        try:
            parses=a.getfloat(0,l)/a.dur
            execs=a.getfloat(1,l)/a.dur
            percent=a.getfloat(2,l)
            a.sqlid=a.getstring(3,l).lstrip()
        except: return
        d=dict(timestamp='text',sqlid='text',parses='real',execs='real',percent='real')
        v=dict(timestamp=a.date,sqlid=a.sqlid,parses=parses,execs=execs,percent=percent)
        if 'DBORASQP' in a.scope: a.emit('DBORASQP', d, v)
        a.state='mod'
        a.setContext('mod')
        a.request=''

    def asqm(s, a, l, g, m):
        flag=False
        try:
            x=a.getstring(5,l)
            flag=True
        except: pass
        try:
            sharedmem=a.getfloat(1,l) if flag else a.getfloat(0,l)
            execs=a.getfloat(3,l)/a.dur if flag else a.getfloat(1,l)/a.dur
            percent=a.getfloat(4,l) if flag else a.getfloat(2,l)
            a.sqlid=a.getstring(5,l).lstrip() if flag else a.getstring(3,l).lstrip()
        except: return
        d=dict(timestamp='text',sqlid='text',sharedmem='real',execs='real',percent='real')
        v=dict(timestamp=a.date,sqlid=a.sqlid,sharedmem=sharedmem,execs=execs,percent=percent)
        if 'DBORASQM' in a.scope: a.emit('DBORASQM', d, v)
        a.state='mod'
        a.setContext('mod')
        a.request=''

    def asqv(s, a, l, g, m):
        flag=False
        try:
            x=a.getstring(4,l)
            flag=True
        except: pass
        try:
            versioncount=a.getfloat(1,l) if flag else a.getfloat(0,l)
            execs=a.getfloat(3,l)/a.dur if flag else a.getfloat(1,l)/a.dur
            a.sqlid=a.getstring(4,l).lstrip() if flag else a.getstring(2,l).lstrip()
        except: return
        d=dict(timestamp='text',sqlid='text',versioncount='real',execs='real')
        v=dict(timestamp=a.date,sqlid=a.sqlid,versioncount=versioncount,execs=execs)
        if 'DBORASQV' in a.scope: a.emit('DBORASQV', d, v)
        a.state='mod'
        a.setContext('mod')
        a.request=''

    def asqw(s, a, l, g, m):
        try:
            clusterwait=a.getfloat(0,l)/a.dur
            elapsed=a.getfloat(2,l)/a.dur
            cpu=a.getfloat(3,l)/a.dur
            execs=a.getfloat(4,l)/a.dur
            a.sqlid=a.getstring(5,l).lstrip()
        except: return
        d=dict(timestamp='text',sqlid='text',clusterwait='real',elapsed='real',cpu='real',execs='real')
        v=dict(timestamp=a.date,sqlid=a.sqlid,clusterwait=clusterwait,elapsed=elapsed,cpu=cpu,execs=execs)
        if 'DBORASQW' in a.scope: a.emit('DBORASQW', d, v)
        a.state='mod'
        a.setContext('mod')
        a.request=''

    def asqg(s, a, l, g, m):
        if a.type=='STATSPACK_8I':
            try:
                gets=a.getfloat(0,l)/a.dur
                execs=a.getfloat(1,l)/a.dur
                percent=a.getfloat(3,l)
                cpu=0.0
                elapsed=0.0
                a.sqlid=a.getstring(4,l).lstrip()
            except: return
        else:
            try:
                gets=a.getfloat(0,l)/a.dur
                execs=a.getfloat(1,l)/a.dur
                percent=a.getfloat(3,l)
                elapsed=a.getfloat(4,l)/a.dur if '11.2' in a.version  or '12.1' in a.version else a.getfloat(5,l)/a.dur
                cpu=elapsed*a.getfloat(5,l)/100 if '11.2' in a.version  or '12.1' in a.version else a.getfloat(4,l)/a.dur
                a.sqlid=a.getstring(6,l).lstrip()
                a.sqlid=a.getstring(7,l).lstrip() if '11.2' in a.version  or '12.1' in a.version else a.sqlid
            except: return
        d=dict(timestamp='text',sqlid='text',gets='real',execs='real',percent='real',cpu='real',elapsed='real')
        v=dict(timestamp=a.date,sqlid=a.sqlid,gets=gets,execs=execs,percent=percent,cpu=cpu,elapsed=elapsed)
        if 'DBORASQG' in a.scope: a.emit('DBORASQG', d, v)
        a.state='mod'
        a.setContext('mod')
        a.request=''

    def asqr(s, a, l, g, m):
        if a.type=='STATSPACK_8I':
            try:
                reads=a.getfloat(0,l)/a.dur
                execs=a.getfloat(1,l)/a.dur
                percent=a.getfloat(3,l)
                cpu=0.0
                elapsed=0.0
                a.sqlid=a.getstring(4,l).lstrip()
            except: return
        else:
            try:
                reads=a.getfloat(0,l)/a.dur
                execs=a.getfloat(1,l)/a.dur
                percent=a.getfloat(3,l)
                elapsed=a.getfloat(4,l)/a.dur if '11.2' in a.version  or '12.1' in a.version else a.getfloat(5,l)/a.dur
                cpu=elapsed*a.getfloat(5,l)/100 if '11.2' in a.version  or '12.1' in a.version else a.getfloat(4,l)/a.dur
                a.sqlid=a.getstring(6,l).lstrip()
                a.sqlid=a.getstring(7,l).lstrip() if '11.2' in a.version  or '12.1' in a.version else a.sqlid
            except: return
        d=dict(timestamp='text',sqlid='text',reads='real',execs='real',percent='real',cpu='real',elapsed='real')
        v=dict(timestamp=a.date,sqlid=a.sqlid,reads=reads,execs=execs,percent=percent,cpu=cpu,elapsed=elapsed)
        if 'DBORASQR' in a.scope: a.emit('DBORASQR', d, v)
        a.state='mod'
        a.setContext('mod')
        a.request=''

    def asqrp(s, a, l, g, m):
        try:
            requests=a.getfloat(0,l)/a.dur
            reads=a.getfloat(1,l)/a.dur
            execs=a.getfloat(2,l)/a.dur
            percent=a.getfloat(5,l)
            a.sqlid=a.getstring(6,l).lstrip()
        except: return
        d=dict(timestamp='text',sqlid='text',requests='real',reads='real',execs='real',percent='real')
        v=dict(timestamp=a.date,sqlid=a.sqlid,requests=requests,reads=reads,execs=execs,percent=percent)
        if 'DBORASQRP' in a.scope: a.emit('DBORASQRP', d, v)
        a.state='mod'
        a.setContext('mod')
        a.request=''

    def asqx(s, a, l, g, m):
        if a.type=='STATSPACK_8I':
            try:
                execs=a.getfloat(0,l)/a.dur
                rows=a.getfloat(1,l)/a.dur
                cpuperexec=0.0
                elapsedperexec=0.0
                a.sqlid=a.getstring(3,l).lstrip()
            except: return
        else:
            try:
                execs=a.getfloat(0,l)/a.dur
                rows=a.getfloat(1,l)/a.dur
                elapsedperexec=a.getfloat(3,l)/execs if '11.2' in a.version  or '12.1' in a.version else a.getfloat(4,l)
                cpuperexec=elapsedperexec*a.getfloat(4,l)/100 if '11.2' in a.version  or '12.1' in a.version else a.getfloat(3,l)
                a.sqlid=a.getstring(5,l).lstrip()
                a.sqlid=a.getstring(6,l).lstrip() if '11.2' in a.version  or '12.1' in a.version else a.sqlid
            except: return
        d=dict(timestamp='text',sqlid='text',execs='real',rows='real',cpuperexec='real',elapsedperexec='real')
        v=dict(timestamp=a.date,sqlid=a.sqlid,execs=execs,rows=rows,cpuperexec=cpuperexec,elapsedperexec=elapsedperexec)
        if 'DBORASQX' in a.scope: a.emit('DBORASQX', d, v)
        a.state='mod'
        a.setContext('mod')
        a.request=''

    def aoss(s, a, l, g, m):
        try:
            statistic=a.getstring(0,l)
            value=a.getfloat(1,l)
        except: return
        d=dict(timestamp='text',statistic='text',value='real')
        v=dict(timestamp=a.date,statistic=statistic,value=value)
        a.emit('DBORAOSS', d, v)

    def asrv(s, a, l, g, m):
        try:
            service=a.getstring(0,l)
            dbtime=a.getfloat(1,l)/a.dur
            cpu=a.getfloat(2,l)/a.dur
            reads=a.getfloat(3,l)/a.dur
            gets=a.getfloat(4,l)/a.dur
        except: return
        d=dict(timestamp='text',service='text',dbtime='real',cpu='real',reads='real',gets='real')
        v=dict(timestamp=a.date,service=service,dbtime=dbtime,cpu=cpu,reads=reads,gets=gets)
        a.emit('DBORASRV', d, v)

    def asvw(s, a, l, g, m):
        try:
            uiowaits=a.getfloat(1,l)/a.dur
            uiowaitt=a.getfloat(2,l)/a.dur
            conwaits=a.getfloat(3,l)/a.dur
            conwaitt=a.getfloat(4,l)/a.dur
            admwaits=a.getfloat(5,l)/a.dur
            admwaitt=a.getfloat(6,l)/a.dur
            netwaits=a.getfloat(7,l)/a.dur
            netwaitt=a.getfloat(8,l)/a.dur
        except: return
        service=a.pattern
        d=dict(timestamp='text',service='text',uiowaits='real',uiowaitt='real',conwaits='real',conwaitt='real',admwaits='real',admwaitt='real',netwaits='real',netwaitt='real')
        v=dict(timestamp=a.date,service=service,uiowaits=uiowaits,uiowaitt=uiowaitt,conwaits=conwaits,conwaitt=conwaitt,admwaits=admwaits,admwaitt=admwaitt,netwaits=netwaits,netwaitt=netwaitt)
        a.emit('DBORASVW', d, v)

    def abuf(s, a, l, g, m):
        if a.type=='STATSPACK_8I':
            try:
                bufpool=a.getstring(0,l)
                gets=(a.getfloat(1,l)+a.getfloat(2,l))/a.dur
                reads=a.getfloat(3,l)/a.dur
                writes=a.getfloat(4,l)/a.dur
                freewaits=a.getfloat(5,l)/a.dur
                writecompletewaits=a.getfloat(6,l)/a.dur
                busywaits=a.getfloat(7,l)/a.dur
            except: return
        else:
            try:
                bufpool=a.getstring(0,l)
                gets=a.getfloat(3,l)/a.dur
                reads=a.getfloat(4,l)/a.dur
                writes=a.getfloat(5,l)/a.dur
                freewaits=a.getfloat(6,l)/a.dur
                writecompletewaits=a.getfloat(7,l)/a.dur
                busywaits=a.getfloat(8,l)/a.dur
            except: return
        d=dict(timestamp='text',bufpool='text',gets='real',reads='real',writes='real',freewaits='real',writecompletewaits='real',busywaits='real')
        v=dict(timestamp=a.date,bufpool=bufpool,gets=gets,reads=reads,writes=writes,freewaits=freewaits,writecompletewaits=writecompletewaits,busywaits=busywaits)
        a.emit('DBORABUF', d, v)

    def asglr(s, a, l, g, m):
        try:
            owner=a.getstring(0,l)
            tablespace=a.getstring(1,l)
            objname=a.getstring(2,l)
            subobject=a.getstring(3,l)
            objtype=a.getstring(4,l)
            gets=a.getfloat(5,l)/a.dur
        except: return
        d=dict(timestamp='text',owner='text',tablespace='text',object='text',subobject='text',objtype='text',gets='real')
        v=dict(timestamp=a.date,owner=owner,tablespace=tablespace,object=objname,subobject=subobject,objtype=objtype,gets=gets)
        a.emit('DBORASGLR', d, v)

    def asgpr(s, a, l, g, m):
        try:
            owner=a.getstring(0,l)
            tablespace=a.getstring(1,l)
            objname=a.getstring(2,l)
            subobject=a.getstring(3,l)
            objtype=a.getstring(4,l)
            reads=a.getfloat(5,l)/a.dur
        except: return
        d=dict(timestamp='text',owner='text',tablespace='text',object='text',subobject='text',objtype='text',reads='real')
        v=dict(timestamp=a.date,owner=owner,tablespace=tablespace,object=objname,subobject=subobject,objtype=objtype,reads=reads)
        a.emit('DBORASGPR', d, v)

    def asgrlw(s, a, l, g, m):
        try:
            owner=a.getstring(0,l)
            tablespace=a.getstring(1,l)
            objname=a.getstring(2,l)
            subobject=a.getstring(3,l)
            objtype=a.getstring(4,l)
            waits=a.getfloat(5,l)/a.dur
        except: return
        d=dict(timestamp='text',owner='text',tablespace='text',object='text',subobject='text',objtype='text',waits='real')
        v=dict(timestamp=a.date,owner=owner,tablespace=tablespace,object=objname,subobject=subobject,objtype=objtype,waits=waits)
        a.emit('DBORASGRLW', d, v)

    def asgcrbr(s, a, l, g, m):
        try:
            owner=a.getstring(0,l)
            tablespace=a.getstring(1,l)
            objname=a.getstring(2,l)
            subobject=a.getstring(3,l)
            objtype=a.getstring(4,l)
            blocks=a.getfloat(5,l)/a.dur
        except: return
        d=dict(timestamp='text',owner='text',tablespace='text',object='text',subobject='text',objtype='text',blocks='real')
        v=dict(timestamp=a.date,owner=owner,tablespace=tablespace,object=objname,subobject=subobject,objtype=objtype,blocks=blocks)
        a.emit('DBORASGCRBR', d, v)

    def asgcbr(s, a, l, g, m):
        try:
            owner=a.getstring(0,l)
            tablespace=a.getstring(1,l)
            objname=a.getstring(2,l)
            subobject=a.getstring(3,l)
            objtype=a.getstring(4,l)
            blocks=a.getfloat(5,l)/a.dur
        except: return
        d=dict(timestamp='text',owner='text',tablespace='text',object='text',subobject='text',objtype='text',blocks='real')
        v=dict(timestamp=a.date,owner=owner,tablespace=tablespace,object=objname,subobject=subobject,objtype=objtype,blocks=blocks)
        a.emit('DBORASGCBR', d, v)

    def asgiw(s, a, l, g, m):
        try:
            owner=a.getstring(0,l)
            tablespace=a.getstring(1,l)
            objname=a.getstring(2,l)
            subobject=a.getstring(3,l)
            objtype=a.getstring(4,l)
            waits=a.getfloat(5,l)/a.dur
        except: return
        d=dict(timestamp='text',owner='text',tablespace='text',object='text',subobject='text',objtype='text',waits='real')
        v=dict(timestamp=a.date,owner=owner,tablespace=tablespace,object=objname,subobject=subobject,objtype=objtype,waits=waits)
        a.emit('DBORASGIW', d, v)

    def asgbbw(s, a, l, g, m):
        try:
            owner=a.getstring(0,l)
            tablespace=a.getstring(1,l)
            objname=a.getstring(2,l)
            subobject=a.getstring(3,l)
            objtype=a.getstring(4,l)
            waits=a.getfloat(5,l)/a.dur
        except: return
        d=dict(timestamp='text',owner='text',tablespace='text',object='text',subobject='text',objtype='text',waits='real')
        v=dict(timestamp=a.date,owner=owner,tablespace=tablespace,object=objname,subobject=subobject,objtype=objtype,waits=waits)
        a.emit('DBORASGBBW', d, v)

    def asgfsc(s, a, l, g, m):
        try:
            owner=a.getstring(0,l)
            tablespace=a.getstring(1,l)
            objname=a.getstring(2,l)
            subobject=a.getstring(3,l)
            objtype=a.getstring(4,l)
            scans=a.getfloat(5,l)/a.dur
        except: return
        d=dict(timestamp='text',owner='text',tablespace='text',object='text',subobject='text',objtype='text',scans='real')
        v=dict(timestamp=a.date,owner=owner,tablespace=tablespace,object=objname,subobject=subobject,objtype=objtype,scans=scans)
        a.emit('DBORASGFSC', d, v)

    def asggcbb(s, a, l, g, m):
        try:
            owner=a.getstring(0,l)
            tablespace=a.getstring(1,l)
            objname=a.getstring(2,l)
            subobject=a.getstring(3,l)
            objtype=a.getstring(4,l)
            waits=a.getfloat(5,l)/a.dur
        except: return
        d=dict(timestamp='text',owner='text',tablespace='text',object='text',subobject='text',objtype='text',waits='real')
        v=dict(timestamp=a.date,owner=owner,tablespace=tablespace,object=objname,subobject=subobject,objtype=objtype,waits=waits)
        a.emit('DBORASGGCBB', d, v)
