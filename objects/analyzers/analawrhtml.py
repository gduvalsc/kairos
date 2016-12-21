class UserObject(dict):
    def __init__(s):
        object = {
            "type": "analyzer",
            "id": "ANALAWRHTML",
            "content": "xml",
            "begin": s.begin,
            "end": s.end,
            "rules": [
                {"action": s.ah3, "regexp": '', "tag": 'h3'},
                {"action": s.atable, "regexp": '', "tag": 'table'},
                {"action": s.atr, "regexp": '', "tag": 'tr'},
                {"action": s.athd, "regexp": '', "tag": '(th|td)'}
            ],
            "contextrules": [
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdbuf", "scope": "DBORABUF"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdbpa", "scope": "DBORABPA"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdenq", "scope": "DBORAENQ"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdfil", "scope": "DBORAFIL"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdlat", "scope": "DBORALAT"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdlaw", "scope": "DBORALAW"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdlib", "scope": "DBORALIB"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdmtt", "scope": "DBORAMTT"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdoss", "scope": "DBORAOSS"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdpga", "scope": "DBORAPGA"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdpgb", "scope": "DBORAPGB"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdpgc", "scope": "DBORAPGC"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdreq", "scope": "DBORAREQ"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsga", "scope": "DBORASGA"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsglr", "scope": "DBORASGLR"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgpr", "scope": "DBORASGPR"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgprr", "scope": "DBORASGPRR"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgur", "scope": "DBORASGUR"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgor", "scope": "DBORASGOR"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgdpr", "scope": "DBORASGDPR"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgpw", "scope": "DBORASGPW"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgpwr", "scope": "DBORASGPWR"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgdpw", "scope": "DBORASGDPW"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgts", "scope": "DBORASGTS"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgdbc", "scope": "DBORASGDBC"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgrlw", "scope": "DBORASGRLW"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgiw", "scope": "DBORASGIW"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgbbw", "scope": "DBORASGBBW"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsggcbb", "scope": "DBORASGGCBB"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgcrbr", "scope": "DBORASGCRBR"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsgcbr", "scope": "DBORASGCBR"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsqc", "scope": "DBORASQC"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsqe", "scope": "DBORASQE"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsqg", "scope": "DBORASQG"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsqm", "scope": "DBORASQM"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsqp", "scope": "DBORASQP"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsqr", "scope": "DBORASQR"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsqv", "scope": "DBORASQV"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsqw", "scope": "DBORASQW"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsqx", "scope": "DBORASQX"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsrv", "scope": "DBORASRV"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsvw", "scope": "DBORASVW"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdsta", "scope": "DBORASTA"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdtab1"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdtab2"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdtbs", "scope": "DBORATBS"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdtms", "scope": "DBORATMS"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdweb", "scope": "DBORAWEB"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdwec", "scope": "DBORAWEC"},
                {"action": s.atdget, "regexp": '', "tag": 'td', "context": "tdwev", "scope": "DBORAWEV"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thbuf", "scope": "DBORABUF"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thbpa", "scope": "DBORABPA"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thenq", "scope": "DBORAENQ"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thfil", "scope": "DBORAFIL"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thlat", "scope": "DBORALAT"},
                {"action": s.athget, "regexp": 'Latch|Time', "tag": 'th', "context": "thlaw", "scope": "DBORALAW"},
                {"action": s.athget, "regexp": '(Namespace|Requests|Reloads|Invali)', "tag": 'th', "context": "thlib", "scope": "DBORALIB"},
                {"action": s.athget, "regexp": '', "tag": 'th', "context": "thmtt", "scope": "DBORAMTT"},
                {"action": s.athget, "regexp": '', "tag": 'th', "context": "thoss", "scope": "DBORAOSS"},
                {"action": s.athget, "regexp": '', "tag": 'th', "context": "thpga", "scope": "DBORAPGA"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thpgb", "scope": "DBORAPGB"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thpgc", "scope": "DBORAPGC"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "threq", "scope": "DBORAREQ"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsga", "scope": "DBORASGA"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsglr", "scope": "DBORASGLR"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgpr", "scope": "DBORASGPR"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgprr", "scope": "DBORASGPRR"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgur", "scope": "DBORASGUR"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgor", "scope": "DBORASGOR"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgdpr", "scope": "DBORASGDPR"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgpw", "scope": "DBORASGPW"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgpwr", "scope": "DBORASGPWR"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgdpw", "scope": "DBORASGDPW"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgts", "scope": "DBORASGTS"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgdbc", "scope": "DBORASGDBC"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgrlw", "scope": "DBORASGRLW"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgiw", "scope": "DBORASGIW"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgbbw", "scope": "DBORASGBBW"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsggcbb", "scope": "DBORASGGCBB"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgcrbr", "scope": "DBORASGCRBR"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsgcbr", "scope": "DBORASGCBR"},
                {"action": s.athget, "regexp": '(.+Time.+|Executions|.+Total|SQL.+)', "tag": 'th', "context": "thsqc", "scope": "DBORASQC"},
                {"action": s.athget, "regexp": '(.+Time.+|Executions|.+Total|SQL.+|CPU)', "tag": 'th', "context": "thsqe", "scope": "DBORASQE"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsqg", "scope": "DBORASQG"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsqm", "scope": "DBORASQM"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsqp", "scope": "DBORASQP"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsqr", "scope": "DBORASQR"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsqv", "scope": "DBORASQV"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsqw", "scope": "DBORASQW"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsqx", "scope": "DBORASQX"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsrv", "scope": "DBORASRV"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsvw", "scope": "DBORASVW"},
                {"action": s.athget, "regexp": '(Statistic|Total)', "tag": 'th', "context": "thsta", "scope": "DBORASTA"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thtab1"},
                {"action": s.athget, "regexp": '', "tag": 'th', "context": "thtab2"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thtbs", "scope": "DBORATBS"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thtms", "scope": "DBORATMS"},
                {"action": s.athget, "regexp": '(Event|Waits$|Total Wait Time.+|%Time -outs)', "tag": 'th', "context": "thweb", "scope": "DBORAWEB"},
                {"action": s.athget, "regexp": '(Wait Class|Waits$|Total Wait Time.+|%Time -outs)', "tag": 'th', "context": "thwec", "scope": "DBORAWEC"},
                {"action": s.athget, "regexp": '(Event|Waits$|Total Wait Time.+|%Time -outs)', "tag": 'th', "context": "thwev", "scope": "DBORAWEV"}
            ],
            "outcontextrules": [
                {"action": s.genstate('thweb'), "regexp": 'Background Wait Events', "tag": 'h3', "scope": "DBORAWEB"},
                {"action": s.genstate('thbuf'), "regexp": 'Buffer Pool Statistics', "tag": 'h3', "scope": "DBORABUF"},
                {"action": s.genstate('threq'), "regexp": 'Complete List of SQL Text', "tag": 'h3', "scope": "DBORAREQ"},
                {"action": s.genstate('thenq'), "regexp": 'Enqueue Activity', "tag": 'h3', "scope": "DBORAENQ"},
                {"action": s.genstate('thfil'), "regexp": 'File IO Stats', "tag": 'h3', "scope": "DBORAFIL"},
                {"action": s.genstate('thwec'), "regexp": 'Foreground Wait Class', "tag": 'h3', "scope": "DBORAWEC"},
                {"action": s.genstate('thwev'), "regexp": 'Foreground Wait Events', "tag": 'h3', "scope": "DBORAWEV"},
                {"action": s.genstate('thsta'), "regexp": 'Instance Activity Stats', "tag": 'h3', "scope": "DBORASTA"},
                {"action": s.genstate('thmtt'), "regexp": 'Instance Recovery Stats', "tag": 'h3', "scope": "DBORAMTT"},
                {"action": s.genstate('thlaw'), "regexp": 'Latch Activity', "tag": 'h3', "scope": "DBORALAW"},
                {"action": s.genstate('thlat'), "regexp": 'Latch Sleep Breakdown', "tag": 'h3', "scope": "DBORALAT"},
                {"action": s.genstate('thlib'), "regexp": 'Library Cache Activity', "tag": 'h3', "scope": "DBORALIB"},
                {"action": s.genstate('thoss'), "regexp": 'Operating System Statistics', "tag": 'h3', "scope": "DBORAOSS"},
                {"action": s.genstate('thpgb'), "regexp": 'PGA Aggr Summary', "tag": 'h3', "scope": "DBORAPGB"},
                {"action": s.genstate('thpgc'), "regexp": 'PGA Aggr Target Histogram', "tag": 'h3', "scope": "DBORAPGC"},
                {"action": s.genstate('thpga'), "regexp": 'PGA Aggr Target Stats', "tag": 'h3', "scope": "DBORAPGA"},
                {"action": s.genstate('thsglr'), "regexp": 'Segments by Logical Reads', "tag": 'h3', "scope": "DBORASGLR"},
                {"action": s.genstate('thsgpr'), "regexp": 'Segments by Physical Reads', "tag": 'h3', "scope": "DBORASGPR"},
                {"action": s.genstate('thsgprr'), "regexp": 'Segments by Physical Read Requests', "tag": 'h3', "scope": "DBORASGPRR"},
                {"action": s.genstate('thsgur'), "regexp": 'Segments by UnOptimized Reads', "tag": 'h3', "scope": "DBORASGUR"},
                {"action": s.genstate('thsgor'), "regexp": 'Segments by Optimized Reads', "tag": 'h3', "scope": "DBORASGOR"},
                {"action": s.genstate('thsgdpr'), "regexp": 'Segments by Direct Physical Reads', "tag": 'h3', "scope": "DBORASGDPR"},
                {"action": s.genstate('thsgpw'), "regexp": 'Segments by Physical Writes', "tag": 'h3', "scope": "DBORASGPW"},
                {"action": s.genstate('thsgpwr'), "regexp": 'Segments by Physical Write Requests', "tag": 'h3', "scope": "DBORASGPWR"},
                {"action": s.genstate('thsgdpw'), "regexp": 'Segments by Direct Physical Writes', "tag": 'h3', "scope": "DBORASGDPW"},
                {"action": s.genstate('thsgts'), "regexp": 'Segments by Table Scans', "tag": 'h3', "scope": "DBORASGTS"},
                {"action": s.genstate('thsgdbc'), "regexp": 'Segments by DB Blocks Changes', "tag": 'h3', "scope": "DBORASGDBC"},
                {"action": s.genstate('thsgrlw'), "regexp": 'Segments by Row Lock Waits', "tag": 'h3', "scope": "DBORASGRLW"},
                {"action": s.genstate('thsgiw'), "regexp": 'Segments by ITL Waits', "tag": 'h3', "scope": "DBORASGIW"},
                {"action": s.genstate('thsgbbw'), "regexp": 'Segments by Buffer Busy Waits', "tag": 'h3', "scope": "DBORASGBBW"},
                {"action": s.genstate('thsggcbb'), "regexp": 'Segments by Global Cache Buffer Busy', "tag": 'h3', "scope": "DBORASGGCBB"},
                {"action": s.genstate('thsgcrbr'), "regexp": 'Segments by CR Blocks Received', "tag": 'h3', "scope": "DBORASGCRBR"},
                {"action": s.genstate('thsgcbr'), "regexp": 'Segments by Current Blocks Received', "tag": 'h3', "scope": "DBORASGCBR"},
                {"action": s.genstate('thsrv'), "regexp": 'Service Statistics', "tag": 'h3', "scope": "DBORASRV"},
                {"action": s.genstate('thsvw'), "regexp": 'Service Wait Class Stats', "tag": 'h3', "scope": "DBORASVW"},
                {"action": s.genstate('thsga'), "regexp": 'SGA breakdown difference', "tag": 'h3', "scope": "DBORASGA"},
                {"action": s.genstate('thsqw'), "regexp": 'SQL ordered by Cluster Wait Time', "tag": 'h3', "scope": "DBORASQW"},
                {"action": s.genstate('thsqc'), "regexp": 'SQL ordered by CPU Time', "tag": 'h3', "scope": "DBORASQC"},
                {"action": s.genstate('thsqe'), "regexp": 'SQL ordered by Elapsed Time', "tag": 'h3', "scope": "DBORASQE"},
                {"action": s.genstate('thsqp'), "regexp": 'SQL ordered by Parse Calls', "tag": 'h3', "scope": "DBORASQP"},
                {"action": s.genstate('thsqx'), "regexp": 'SQL ordered by Executions', "tag": 'h3', "scope": "DBORASQX"},
                {"action": s.genstate('thsqg'), "regexp": 'SQL ordered by Gets', "tag": 'h3', "scope": "DBORASQG"},
                {"action": s.genstate('thsqr'), "regexp": 'SQL ordered by Reads', "tag": 'h3', "scope": "DBORASQR"},
                {"action": s.genstate('thsqm'), "regexp": 'SQL ordered by Sharable Memory', "tag": 'h3', "scope": "DBORASQM"},
                {"action": s.genstate('thsqv'), "regexp": 'SQL ordered by Version Count', "tag": 'h3', "scope": "DBORASQV"},
                {"action": s.genstate('thtbs'), "regexp": 'Tablespace IO Stats', "tag": 'h3', "scope": "DBORATBS"},
                {"action": s.genstate('thtms'), "regexp": 'Time Model Statistics', "tag": 'h3', "scope": "DBORATMS"},
                {"action": s.genstate('thbpa'), "regexp": 'Buffer Pool Advisory', "tag": 'h3', "scope": "DBORABPA"},
                #{"action": s.genstate('thtab1'), "regexp": 'DB NameDB IdInstanceInst numStartup TimeReleaseRAC', "tag": 'tr'},
                {"action": s.genstate('thtab1'), "regexp": 'DB Name', "tag": 'th'},
                #{"action": s.genstate('thtab2'), "regexp": 'Snap IdSnap TimeSessionsCursors/Session', "tag": 'tr'}
                {"action": s.genstate('thtab2'), "regexp": 'Snap Id', "tag": 'th'}
            ]
        }
        super(UserObject, s).__init__(**object)
    def begin(s, a):
        a.collector = {}
        a.cpt = -1
        a.collected = {}
        a.row = {}
        a.reinit = True
        a.sqlid = {}
        a.month = dict(Jan='01',Feb='02',Fev='02',Mar='03',Apr='04',Avr='04',May='05',Mai='05', Jun='06',Jul='07',Aug='08',Sep='09',Oct='10',Nov='11',Dec='12')
        a.setContext('');
    def end(s, a):
        tof=lambda x: float(x.replace(',','').replace(u'\xa0','0')) if x!=u'' else 0.0
        toc=lambda x: x.replace('&quot;',"'").replace('&lt;',"<").replace('&gt;',">").replace(u'\xa0','')
        for x in sorted(a.collected.keys(),reverse=True):
            line=-1
            if x =='zz9':
                dinfo = dict(timestamp='text', startup='text')
                for y in a.collected[x]:
                    a.version = y['Release']
                    a.startup = y['Startup Time']
            if x =='zz8':
                dmisc = dict(timestamp='text', type='text', sessions='real', avgelapsed='real', elapsed='int')
                for y in a.collected[x]:
                    when = y['']
                    what = y['Snap Time']
                    if when == 'End Snap:':
                        year = str('20' + what[7:9])
                        month = a.month[str(what[3:6])]
                        day = str(what[0:2])
                        hour = str(what[10:12])
                        min = str(what[13:15])
                        sec = str(what[16:18])
                        a.date = year + month + day + hour + min + sec + "000"
                        a.sessions = int(tof(y['Sessions']))
                    if when == 'Elapsed:':
                        a.dur = int(tof(what[:-6])*60)
                        type='AWR_11G'
                        if 'DBORAMISC' in a.scope: a.emit('DBORAMISC', dmisc, dict(timestamp=a.date, type=type, sessions=a.sessions, avgelapsed=a.dur, elapsed=int(a.dur)))
                        if 'DBORAINFO' in a.scope: a.emit('DBORAINFO', dinfo, dict(timestamp=a.date, startup=a.startup))
            if x == 'Foreground Wait Events':
                d = dict(timestamp='text', event='text', count='real', timeouts='real', time='real')
                for y in a.collected[x]:
                    event = y['Event']
                    count = tof(y['Waits']) / a.dur
                    timeouts = tof(y['%Time -outs']) * count / 100
                    time = tof(y['Total Wait Time (s)']) / a.dur
                    a.emit('DBORAWEV', d, dict(timestamp=a.date, event=event, count=count, timeouts=timeouts, time=time))
            if x == 'Background Wait Events':
                d = dict(timestamp='text',event='text',count='real',timeouts='real',time='real')
                for y in a.collected[x]:
                    event = y['Event']
                    count = tof(y['Waits']) / a.dur
                    timeouts = tof(y['%Time -outs']) * count / 100
                    time = tof(y['Total Wait Time (s)']) / a.dur
                    a.emit('DBORAWEB', d, dict(timestamp=a.date, event=event, count=count, timeouts=timeouts, time=time))
            if x == 'Foreground Wait Class':
                d = dict(timestamp='text',eclass='text',count='real',timeouts='real',time='real')
                for y in a.collected[x]:
                    eclass = y['Wait Class']
                    count = tof(y['Waits']) / a.dur
                    timeouts = tof(y['%Time -outs']) * count / 100
                    time = tof(y['Total Wait Time (s)']) / a.dur
                    a.emit('DBORAWEC', d, dict(timestamp=a.date, eclass=eclass, count=count, timeouts=timeouts, time=time))
            if x in ('Instance Activity Stats','Key Instance Activity Stats','Other Instance Activity Stats','Instance Activity Stats - Thread Activity'):
                d = dict(timestamp='text',statistic='text',value='real')
                for y in a.collected[x]:
                    name = y['Statistic']
                    value = tof(y['Total']) / a.dur
                    a.emit('DBORASTA', d, dict(timestamp=a.date, statistic=name, value=value))
            if x == 'Instance Recovery Stats':
                d = dict(timestamp='text', targetmttr='real', estdmttr='real', recovestdios='real', actualredoblks='real', targetredoblks='real', logszredoblks='real', logckpttimeoutredoblks='real', logckptintervalredoblks='real', optlogsz='real', estdracavailtime='real')
                for y in a.collected[x]:
                    when = y['']
                    if when == 'E':
                        f1 = tof(y['Targt MTTR  (s)'])
                        f2 = tof(y['Estd MTTR (s)'])
                        f3 = tof(y['Recovery Estd IOs'])
                        try: f4 = tof(y['Actual  RedoBlks'])
                        except: f4 = tof(y['Actual   Redo Blks'])
                        try: f5 = tof(y['Target  RedoBlks'])
                        except: f5 = tof(y['Target   Redo Blks'])
                        try: f6 = tof(y['Log Sz  RedoBlks'])
                        except: f6 = tof(y['Log File Size   Redo Blks'])
                        try: f7 = tof(y['Log Ckpt Timeout RedoBlks'])
                        except: f7 = tof(y['Log Ckpt  Timeout  Redo Blks'])
                        try: f8 = tof(y['Log Ckpt Interval RedoBlks'])
                        except: f8 = tof(y['Log Ckpt  Interval  Redo Blks'])
                        try: f9 = tof(y['Opt Log Sz(M)'])
                        except: f9 = None
                        try: f10 = tof(y['Estd RAC Avail Time'])
                        except: f10 = None
                        a.emit('DBORAMTT', d, dict(timestamp=a.date, targetmttr=f1, estdmttr=f2, recovestdios=f3, actualredoblks=f4, targetredoblks=f5, logszredoblks=f6, logckpttimeoutredoblks=f7, logckptintervalredoblks=f8, optlogsz=f9, estdracavailtime=f10))
            if x == 'Library Cache Activity':
                d = dict(timestamp='text', item='text', gets='real', pins='real', reloads='real', invalidations='real')
                for y in a.collected[x]:
                    item = y['Namespace']
                    gets = tof(y['Get Requests']) / a.dur
                    pins = tof(y['Pin Requests']) / a.dur
                    reloads = tof(y['Reloads']) / a.dur
                    invalidations = tof(y['Invali- dations']) / a.dur
                    a.emit('DBORALIB', d, dict(timestamp=a.date, item=item, gets=gets, pins=pins, reloads=reloads, invalidations=invalidations))
            if x == 'SQL ordered by Elapsed Time':
                d = dict(timestamp='text', sqlid='text', reads='real', execs='real', cpu='real', elapsed='real', percent='real')
                for y in a.collected[x]:
                    elapsed = tof(y['Elapsed  Time (s)']) / a.dur
                    try: cpu = (tof(y['%CPU']) * elapsed) / 100
                    except: cpu = tof(y['CPU    Time (s)'])
                    execs = tof(y['Executions']) / a.dur
                    try: percent = tof(y['%Total'])
                    except: percent = tof(y['% Total DB Time'])
                    sqlid = y['SQL Id']
                    a.sqlid[sqlid] = y['SQL Module']
                    reads=0.0
                    a.emit('DBORASQE', d, dict(timestamp=a.date, sqlid=sqlid, reads=reads, execs=execs, cpu=cpu, elapsed=elapsed, percent=percent))
            if x == 'SQL ordered by Parse Calls':
                d = dict(timestamp='text', sqlid='text', parses='real', execs='real', percent='real')
                for y in a.collected[x]:
                    parses = tof(y['Parse Calls']) / a.dur
                    execs = tof(y['Executions']) / a.dur
                    percent = tof(y['% Total Parses'])
                    sqlid = y['SQL Id']
                    a.sqlid[sqlid] = y['SQL Module']
                    a.emit('DBORASQP', d, dict(timestamp=a.date, sqlid=sqlid, parses=parses, execs=execs, percent=percent))
            if x == 'SQL ordered by Sharable Memory':
                d = dict(timestamp='text', sqlid='text', sharedmem='real', execs='real', percent='real')
                for y in a.collected[x]:
                    sharedmem = tof(y['Sharable Mem (b)'])
                    execs = tof(y['Executions']) / a.dur
                    percent = tof(y['% Total'])
                    sqlid = y['SQL Id']
                    a.sqlid[sqlid] = y['SQL Module']
                    a.emit('DBORASQM', d, dict(timestamp=a.date, sqlid=sqlid, sharedmem=sharedmem, execs=execs, percent=percent))
            if x == 'SQL ordered by Version Count':
                d = dict(timestamp='text', sqlid='text', versioncount='real', execs='real')
                for y in a.collected[x]:
                    versioncount = tof(y['Version Count'])
                    execs = tof(y['Executions']) / a.dur
                    sqlid = y['SQL Id']
                    a.sqlid[sqlid] = y['SQL Module']
                    a.emit('DBORASQV', d, dict(timestamp=a.date, sqlid=sqlid, versioncount=versioncount, execs=execs))
            if x == 'SQL ordered by Cluster Wait Time':
                d = dict(timestamp='text', sqlid='text', clusterwait='real', elapsed='real', cpu='real', execs='real')
                for y in a.collected[x]:
                    execs = tof(y['Executions']) / a.dur
                    clusterwait = tof(y['Cluster Wait Time (s)']) / a.dur
                    elapsed = tof(y['Elapsed Time(s)']) / a.dur
                    try: cpu = tof(y['%CPU']) * elapsed / 100
                    except: cpu = tof(y['CPU    Time (s)'])
                    sqlid = y['SQL Id']
                    a.sqlid[sqlid] = y['SQL Module']
                    a.emit('DBORASQW', d, dict(timestamp=a.date, sqlid=sqlid, clusterwait=clusterwait, elapsed=elapsed, cpu=cpu, execs=execs))
            if x == 'SQL ordered by Gets':
                d = dict(timestamp='text', sqlid='text', gets='real', execs='real', percent='real', cpu='real', elapsed='real')
                for y in a.collected[x]:
                    gets = tof(y['Buffer Gets']) / a.dur
                    execs = tof(y['Executions']) / a.dur
                    percent = tof(y['%Total'])
                    elapsed = tof(y['Elapsed  Time (s)']) / a.dur
                    try: cpu = tof(y['%CPU']) * elapsed / 100
                    except: cpu = tof(y['CPU    Time (s)'])
                    sqlid = y['SQL Id']
                    a.sqlid[sqlid] = y['SQL Module']
                    a.emit('DBORASQG', d, dict(timestamp=a.date, sqlid=sqlid, gets=gets, execs=execs, percent=percent, cpu=cpu, elapsed=elapsed))
            if x == 'SQL ordered by Reads':
                d = dict(timestamp='text', sqlid='text', reads='real', execs='real', percent='real', cpu='real', elapsed='real')
                for y in a.collected[x]:
                    reads = tof(y['Physical Reads']) / a.dur
                    execs = tof(y['Executions']) / a.dur
                    percent = tof(y['%Total'])
                    elapsed = tof(y['Elapsed  Time (s)']) / a.dur
                    try: cpu = tof(y['%CPU']) * elapsed
                    except: cpu = tof(y['CPU    Time (s)'])
                    sqlid = y['SQL Id']
                    a.sqlid[sqlid] = y['SQL Module']
                    a.emit('DBORASQR', d, dict(timestamp=a.date, sqlid=sqlid, reads=reads, execs=execs, percent=percent, cpu=cpu, elapsed=elapsed))
            if x == 'SQL ordered by Executions':
                d = dict(timestamp='text', sqlid='text', execs='real', rows='real', cpuperexec='real', elapsedperexec='real')
                for y in a.collected[x]:
                    rows = tof(y['Rows Processed']) / a.dur
                    execs = tof(y['Executions']) / a.dur
                    try: elapsed = tof(y['Elapsed  Time (s)']) / a.dur
                    except: elapsed = tof(y['Elap per  Exec (s)']) * execs
                    try: cpuperexec = tof(y['%CPU']) * elapsed / execs
                    except: cpuperexec = tof(y['CPU per  Exec (s)']) * execs
                    elapsedperexec = elapsed / execs
                    sqlid = y['SQL Id']
                    a.sqlid[sqlid] = y['SQL Module']
                    a.emit('DBORASQX', d, dict(timestamp=a.date, sqlid=sqlid, execs=execs, rows=rows, cpuperexec=cpuperexec, elapsedperexec=elapsedperexec))
            if x == 'SQL ordered by CPU Time':
                d = dict(timestamp='text', sqlid='text', gets='real', execs='real', cpu='real', elapsed='real', percent='real')
                for y in a.collected[x]:
                    cpu = tof(y['CPU    Time (s)']) / a.dur
                    elapsed = tof(y['Elapsed  Time (s)']) / a.dur
                    execs = tof(y['Executions']) / a.dur
                    try: percent = tof(y['%Total'])
                    except: percent = tof(y['% Total DB Time'])
                    sqlid = y['SQL Id']
                    a.sqlid[sqlid] = y['SQL Module']
                    gets = 0.0
                    a.emit('DBORASQC', d, dict(timestamp=a.date, sqlid=sqlid, gets=gets, execs=execs, cpu=cpu, elapsed=elapsed, percent=percent))
            if x == 'Complete List of SQL Text':
                d = dict(sqlid='text', module='text', request='text')
                for y in a.collected[x]:
                    sqlid = y['SQL Id']
                    request = toc(y['SQL Text'])
                    module = a.sqlid[sqlid] if sqlid in a.sqlid else ''
                    a.emit('DBORAREQ', d, dict(sqlid=sqlid, module=module, request=request))
            if x == 'Latch Sleep Breakdown':
                d = dict(timestamp='text', latch='text', gets='real', misses='real', sleeps='real')
                for y in a.collected[x]:
                    latch = y['Latch Name']
                    gets = tof(y['Get Requests']) / a.dur
                    misses = tof(y['Misses']) / a.dur
                    sleeps = tof(y['Sleeps']) / a.dur
                    a.emit('DBORALAT', d, dict(timestamp=a.date, latch=latch, gets=gets, misses=misses, sleeps=sleeps))
            if x == 'Latch Activity':
                d = dict(timestamp='text', latch='text', wait='real')
                for y in a.collected[x]:
                    latch = y['Latch Name']
                    wait = tof(y['Wait Time (s)']) / a.dur
                    a.emit('DBORALAW', d, dict(timestamp=a.date, latch=latch, wait=wait))
            if x == 'Enqueue Activity':
                d = dict(timestamp='text', enqueue='text', requests='real', succgets='real', failedgets='real', waits='real', avgwaitpersec='real')
                for y in a.collected[x]:
                    enqueue = y['Enqueue Type (Request Reason)']
                    requests = tof(y['Requests']) / a.dur
                    succgets = tof(y['Succ Gets']) / a.dur
                    failedgets = tof(y['Failed Gets']) / a.dur
                    waits = tof(y['Waits']) / a.dur
                    avgwaitpersec = tof(y['Wt Time (s)']) / a.dur
                    a.emit('DBORAENQ', d, dict(timestamp=a.date, enqueue=enqueue, requests=requests, succgets=succgets, failedgets=failedgets, waits=waits, avgwaitpersec=avgwaitpersec))
            if x == 'Tablespace IO Stats':
                d = dict(timestamp='text', tablespace='text', reads='real', readtime='real', blocksperread='real', writes='real', busy='real', busytime='real')
                for y in a.collected[x]:
                    tablespace = y['Tablespace']
                    reads = tof(y['Reads']) / a.dur
                    readtime = tof(y['Av   Rd(ms)'])
                    blocksperread = tof(y['Av    Blks/Rd'])
                    writes = tof(y['Writes']) / a.dur
                    busy = tof(y['Buffer Waits']) / a.dur
                    busytime = tof(y['Av Buf Wt(ms)'])
                    a.emit('DBORATBS', d, dict(timestamp=a.date, tablespace=tablespace, reads=reads, readtime=readtime, blocksperread=blocksperread, writes=writes, busy=busy, busytime=busytime))
            if x == 'File IO Stats':
                d = dict(timestamp='text', tablespace='text', file='text', reads='real', readtime='real', blocksperread='real', writes='real', busy='real', busytime='real')
                for y in a.collected[x]:
                    tablespace = y['Tablespace']
                    file = y['Filename']
                    reads = tof(y['Reads']) / a.dur
                    readtime = tof(y['Av   Rd(ms)'])
                    blocksperread = tof(y['Av    Blks/Rd'])
                    writes = tof(y['Writes']) / a.dur
                    busy = tof(y['Buffer Waits']) / a.dur
                    busytime = tof(y['Av Buf Wt(ms)'])
                    a.emit('DBORAFIL', d, dict(timestamp=a.date, tablespace=tablespace, file=file, reads=reads, readtime=readtime, blocksperread=blocksperread, writes=writes, busy=busy, busytime=busytime))
            if x == 'SGA breakdown difference':
                d = dict(timestamp='text', pool='text', name='text', size='real')
                for y in a.collected[x]:
                    pool = toc(y['Pool'])
                    name = y['Name']
                    size = tof(y['End MB'])
                    a.emit('DBORASGA', d, dict(timestamp=a.date, pool=pool, name=name, size=size))
            if x == 'PGA Aggr Summary':
                d = dict(timestamp='text', pgahit='real', wamemory='real', extramemory='real')
                for y in a.collected[x]:
                    pgahit = tof(y['PGA Cache Hit %'])
                    wamemory = tof(y['W/A MB Processed']) / a.dur
                    extramemory = tof(y['Extra W/A MB Read/Written']) / a.dur
                    a.emit('DBORAPGB', d, dict(timestamp=a.date, pgahit=pgahit, wamemory=wamemory, extramemory=extramemory))
            if x == 'PGA Aggr Target Stats':
                d = dict(timestamp='text', aggrtarget='real', autotarget='real', memalloc='real', memused='real')
                for y in a.collected[x]:
                    when = y['']
                    if when == 'E':
                        aggrtarget = tof(y['PGA Aggr Target(M)'])
                        autotarget = tof(y['Auto PGA Target(M)'])
                        memalloc = tof(y['PGA Mem  Alloc(M)'])
                        memused = tof(y['W/A PGA  Used(M)'])
                        a.emit('DBORAPGA', d, dict(timestamp=a.date, aggrtarget=aggrtarget, autotarget=autotarget, memalloc=memalloc, memused=memused))
            if x == 'PGA Aggr Target Histogram':
                d = dict(timestamp='text', highoptimal='text', totexecs='real', execs0='real', execs1='real', execs2='real')
                for y in a.collected[x]:
                    highoptimal = y['High Optimal']
                    totexecs = tof(y['Total Execs']) / a.dur
                    execs0 = tof(y['Optimal Execs']) / a.dur
                    execs1 = tof(y['1-Pass Execs']) / a.dur
                    execs2 = tof(y['M-Pass Execs']) / a.dur
                    a.emit('DBORAPGC', d, dict(timestamp=a.date, highoptimal=highoptimal, totexecs=totexecs, execs0=execs0, execs1=execs1, execs2=execs2))
            if x == 'Operating System Statistics':
                d = dict(timestamp='text', statistic='text', value='real')
                for y in a.collected[x]:
                    statistic = y['Statistic']
                    value = tof(y['Value'])
                    a.emit('DBORAOSS', d, dict(timestamp=a.date, statistic=statistic, value=value))
            if x == 'Time Model Statistics':
                d = dict(timestamp='text', statistic='text', time='real')
                for y in a.collected[x]:
                    statistic = y['Statistic Name']
                    time = tof(y['Time (s)']) / a.dur
                    a.emit('DBORATMS', d, dict(timestamp=a.date, statistic=statistic, time=time))
            if x == 'Service Statistics':
                d = dict(timestamp='text', service='text', dbtime='real', cpu='real', reads='real', gets='real')
                for y in a.collected[x]:
                    service = y['Service Name']
                    dbtime = tof(y['DB Time (s)']) / a.dur
                    cpu = tof(y['DB CPU (s)']) / a.dur
                    reads = tof(y['Physical Reads (K)']) / a.dur
                    gets = tof(y['Logical Reads (K)']) / a.dur
                    a.emit('DBORASRV', d, dict(timestamp=a.date, service=service, dbtime=dbtime, cpu=cpu, reads=reads, gets=gets))
            if x == 'Service Wait Class Stats':
                d = dict(timestamp='text', service='text', uiowaits='real', uiowaitt='real', conwaits='real', conwaitt='real', admwaits='real', admwaitt='real', netwaits='real', netwaitt='real')
                for y in a.collected[x]:
                    service = y['Service Name']
                    uiowaits = tof(y['User I/O Total Wts']) / a.dur
                    uiowaitt = tof(y['User I/O Wt Time']) / a.dur
                    conwaits = tof(y['Concurcy Total Wts']) / a.dur
                    conwaitt = tof(y['Concurcy Wt Time']) / a.dur
                    admwaits = tof(y['Admin Total Wts']) / a.dur
                    admwaitt = tof(y['Admin Wt Time']) / a.dur
                    netwaits = tof(y['Network Total Wts']) / a.dur
                    netwaitt = tof(y['Network Wt Time']) / a.dur
                    a.emit('DBORASVW', d, dict(timestamp=a.date, service=service, uiowaits=uiowaits, uiowaitt=uiowaitt, conwaits=conwaits, conwaitt=conwaitt, admwaits=admwaits, admwaitt=admwaitt, netwaits=netwaits, netwaitt=netwaitt))
            if x == 'Buffer Pool Statistics':
                d = dict(timestamp='text', bufpool='text', gets='real', reads='real', writes='real', freewaits='real', writecompletewaits='real', busywaits='real')
                for y in a.collected[x]:
                    bufpool = y['P']
                    gets = tof(y['Buffer Gets']) / a.dur
                    reads = tof(y['Physical Reads']) / a.dur
                    writes = tof(y['Physical Writes']) / a.dur
                    freewaits = tof(y['Free Buff Wait']) / a.dur
                    writecompletewaits = tof(y['Writ Comp Wait']) / a.dur
                    busywaits = tof(y['Buffer Busy Waits']) / a.dur
                    a.emit('DBORABUF', d, dict(timestamp=a.date, bufpool=bufpool, gets=gets, reads=reads, writes=writes, freewaits=freewaits, writecompletewaits=writecompletewaits, busywaits=busywaits))
            if x == 'Buffer Pool Advisory':
                d = dict(timestamp='text', bufpool='text', sizeforest='real', sizefactor='text', buffers='real', estphysreadsfactor='real', estphysreads='real')
                for y in a.collected[x]:
                    bufpool = y['P']
                    sizeforest = tof(y['Size for Est (M)']) * 1024 * 1024
                    sizefactor = str(tof(y['Size Factor']))
                    buffers = tof(y['Buffers (thousands)']) * 1000
                    estphysreadsfactor = tof(y['Est Phys Read Factor'])
                    estphysreads = tof(y['Estimated Phys Reads (thousands)']) / a.dur * 1000
                    a.emit('DBORABPA', d, dict(timestamp=a.date, bufpool=bufpool, sizeforest=sizeforest, sizefactor=sizefactor, buffers=buffers, estphysreadsfactor=estphysreadsfactor, estphysreads=estphysreads))
            if x == 'Segments by Logical Reads':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', gets='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    gets = tof(y['Logical Reads']) / a.dur
                    a.emit('DBORASGLR', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, gets=gets))
            if x == 'Segments by Physical Reads':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', reads='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    reads = tof(y['Physical Reads']) / a.dur
                    a.emit('DBORASGPR', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, reads=reads))
            if x == 'Segments by Physical Read Requests':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', reads='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    reads = tof(y['Phys Read Requests']) / a.dur
                    a.emit('DBORASGPRR', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, reads=reads))
            if x == 'Segments by UnOptimized Reads':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', reads='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    reads = tof(y['UnOptimized Reads']) / a.dur
                    a.emit('DBORASGUR', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, reads=reads))
            if x == 'Segments by Optimized Reads':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', reads='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    reads = tof(y['Optimized Reads']) / a.dur
                    a.emit('DBORASGOR', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, reads=reads))
            if x == 'Segments by Direct Physical Reads':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', reads='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    reads = tof(y['Direct Reads']) / a.dur
                    a.emit('DBORASGDPR', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, reads=reads))
            if x == 'Segments by Physical Writes':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', writes='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    writes = tof(y['Physical Writes']) / a.dur
                    a.emit('DBORASGPW', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, writes=writes))
            if x == 'Segments by Physical Write Requests':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', writes='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    writes = tof(y['Phys Write Requests']) / a.dur
                    a.emit('DBORASGPWR', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, writes=writes))
            if x == 'Segments by Direct Physical Writes':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', writes='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    writes = tof(y['Direct Writes']) / a.dur
                    a.emit('DBORASGDPW', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, writes=writes))
            if x == 'Segments by Table Scans':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', scans='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    scans = tof(y['Table Scans']) / a.dur
                    a.emit('DBORASGTS', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, scans=scans))
            if x == 'Segments by DB Blocks Changes':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', changes='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    changes = tof(y['DB Block Changes']) / a.dur
                    a.emit('DBORASGDBC', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, changes=changes))
            if x == 'Segments by Row Lock Waits':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', waits='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    waits = tof(y['Row Lock Waits']) / a.dur
                    a.emit('DBORASGRLW', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, waits=waits))
            if x == 'Segments by ITL Waits':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', waits='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    waits = tof(y['ITL Waits']) / a.dur
                    a.emit('DBORASGIW', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, waits=waits))
            if x == 'Segments by Buffer Busy Waits':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', waits='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    waits = tof(y['Buffer Busy Waits']) / a.dur
                    a.emit('DBORASGBBW', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, waits=waits))
            if x == 'Segments by Global Cache Buffer Busy':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', waits='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    waits = tof(y['GC Buffer Busy']) / a.dur
                    a.emit('DBORASGGCBB', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, waits=waits))
            if x == 'Segments by CR Blocks Received':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', blocks='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    blocks = tof(y['CR    Blocks  Received']) / a.dur
                    a.emit('DBORASGCRBR', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, blocks=blocks))
            if x == 'Segments by Current Blocks Received':
                d = dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', blocks='real')
                for y in a.collected[x]:
                    owner = y['Owner']
                    tablespace = y['Tablespace    Name']
                    objname = y['Object Name']
                    subobject = y['Subobject   Name']
                    objtype = y['Obj. Type']
                    blocks = tof(y['Current Blocks  Received']) / a.dur
                    a.emit('DBORASGCBR', d, dict(timestamp=a.date, owner=owner, tablespace=tablespace, object=objname, subobject=subobject, objtype=objtype, blocks=blocks))

    def ah3(s, a, l, g, m):
        context = ''
        a.setContext(context)
        if len(a.row): a.tab.append(a.row)
        a.row = {}

    def atable(s, a, l, g, m):
        context = ''
        if a.reinit: a.setContext(context)
        if len(a.scope) < 3:
            if a.scope.issubset({'DBORAINFO', 'DBORAMISC'}) and 'zz9' in a.collected and 'zz8' in a.collected: a.setContext('BREAK')
            if a.scope.issubset({'DBORAWEV'}) and 'Foreground Wait Events' in a.collected and len(a.collected['Foreground Wait Events']): a.setContext('BREAK')
            if a.scope.issubset({'DBORAWEB'}) and 'Background Wait Events' in a.collected and len(a.collected['Background Wait Events']): a.setContext('BREAK')
            if a.scope.issubset({'DBORAWEC'}) and 'Foreground Wait Class' in a.collected and len(a.collected['Foreground Wait Class']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASTA'}) and 'Instance Activity Stats - Thread Activity' in a.collected and len(a.collected['Instance Activity Stats - Thread Activity']): a.setContext('BREAK')
            if a.scope.issubset({'DBORAMTT'}) and 'Instance Recovery Stats' in a.collected and len(a.collected['Instance Recovery Stats']): a.setContext('BREAK')
            if a.scope.issubset({'DBORALIB'}) and 'Library Cache Activity' in a.collected and len(a.collected['Library Cache Activity']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASQE'}) and 'SQL ordered by Elapsed Time' in a.collected and len(a.collected['SQL ordered by Elapsed Time']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASQP'}) and 'SQL ordered by Parse Calls' in a.collected and len(a.collected['SQL ordered by Parse Calls']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASQM'}) and 'SQL ordered by Sharable Memory' in a.collected and len(a.collected['SQL ordered by Sharable Memory']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASQV'}) and 'SQL ordered by Version Count' in a.collected and len(a.collected['SQL ordered by Version Count']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASQW'}) and 'SQL ordered by Cluster Wait Time' in a.collected and len(a.collected['SQL ordered by Cluster Wait Time']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASQG'}) and 'SQL ordered by Gets' in a.collected and len(a.collected['SQL ordered by Gets']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASQR'}) and 'SQL ordered by Reads' in a.collected and len(a.collected['SQL ordered by Reads']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASQX'}) and 'SQL ordered by Executions' in a.collected and len(a.collected['SQL ordered by Executions']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASQC'}) and 'SQL ordered by CPU Time' in a.collected and len(a.collected['SQL ordered by CPU Time']): a.setContext('BREAK')
            if a.scope.issubset({'DBORAREQ'}) and 'Complete List of SQL Text' in a.collected and len(a.collected['Complete List of SQL Text']): a.setContext('BREAK')
            if a.scope.issubset({'DBORALAT'}) and 'Latch Sleep Breakdown' in a.collected and len(a.collected['Latch Sleep Breakdown']): a.setContext('BREAK')
            if a.scope.issubset({'DBORALAW'}) and 'Latch Activity' in a.collected and len(a.collected['Latch Activity']): a.setContext('BREAK')
            if a.scope.issubset({'DBORAENQ'}) and 'Enqueue Activity' in a.collected and len(a.collected['Enqueue Activity']): a.setContext('BREAK')
            if a.scope.issubset({'DBORATBS'}) and 'Tablespace IO Stats' in a.collected and len(a.collected['Tablespace IO Stats']): a.setContext('BREAK')
            if a.scope.issubset({'DBORAFIL'}) and 'File IO Stats' in a.collected and len(a.collected['File IO Stats']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASGA'}) and 'SGA breakdown difference' in a.collected and len(a.collected['SGA breakdown difference']): a.setContext('BREAK')
            if a.scope.issubset({'DBORAPGB'}) and 'PGA Aggr Summary' in a.collected and len(a.collected['PGA Aggr Summary']): a.setContext('BREAK')
            if a.scope.issubset({'DBORAPGA'}) and 'PGA Aggr Target Stats' in a.collected and len(a.collected['PGA Aggr Target Stats']): a.setContext('BREAK')
            if a.scope.issubset({'DBORAPGC'}) and 'PGA Aggr Target Histogram' in a.collected and len(a.collected['PGA Aggr Target Histogram']): a.setContext('BREAK')
            if a.scope.issubset({'DBORAOSS'}) and 'Operating System Statistics' in a.collected and len(a.collected['Operating System Statistics']): a.setContext('BREAK')
            if a.scope.issubset({'DBORATMS'}) and 'Time Model Statistics' in a.collected and len(a.collected['Time Model Statistics']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASRV'}) and 'Service Statistics' in a.collected and len(a.collected['Service Statistics']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASVW'}) and 'Service Wait Class Stats' in a.collected and len(a.collected['Service Wait Class Stats']): a.setContext('BREAK')
            if a.scope.issubset({'DBORABUF'}) and 'Buffer Pool Statistics' in a.collected and len(a.collected['Buffer Pool Statistics']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASGLR'}) and 'Segments by Logical Reads' in a.collected and len(a.collected['Segments by Logical Reads']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASGPR'}) and 'Segments by Physical Reads' in a.collected and len(a.collected['Segments by Physical Reads']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASGRW'}) and 'Segments by Row Lock Waits' in a.collected and len(a.collected['Segments by Row Lock Waits']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASGIW'}) and 'Segments by ITL Waits' in a.collected and len(a.collected['Segments by ITL Waits']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASGFSC'}) and 'Segments by Table Scans' in a.collected and len(a.collected['Segments by Table Scans']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASGBB'}) and 'Segments by Buffer Busy Waits' in a.collected and len(a.collected['Segments by Buffer Busy Waits']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASGGB'}) and 'Segments by Global Cache Buffer Busy' in a.collected and len(a.collected['Segments by Global Cache Buffer Busy']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASGCR'}) and 'Segments by CR Blocks Received' in a.collected and len(a.collected['Segments by CR Blocks Received']): a.setContext('BREAK')
            if a.scope.issubset({'DBORASGCB'}) and 'Segments by Current Blocks Received' in a.collected and len(a.collected['Segments by Current Blocks Received']): a.setContext('BREAK')
        if len(a.row): a.tab.append(a.row)
        a.row = {}
        a.collector = {}

    def athget(s, a, l, g, m):
        if 0 not in a.collector: a.collector[0] = ''
        a.collector[a.cpt]=a.lxmltext(l)

    def atdget(s, a, l, g, m):
        if a.cpt in a.collector: a.row[a.collector[a.cpt]]=a.lxmltext(l)

    def atr(s, a, l, g, m):
        a.reinit = True
        a.cpt = -1
        if hasattr(a,'collector') and len(a.collector): a.setContext('td'+a.context[2:])
        if len(a.row): a.tab.append(a.row)
        a.row = {}

    def athd(s, a, l, g, m):
        a.cpt+=1

    def genstate(s, c):
        def f(a, l ,g, m):
            a.reinit = False
            a.setContext(c)
            a.tab = []
            k = a.lxmltext(l)
            if k == 'DB Name': k = 'zz9'
            if k == 'Snap Id': k = 'zz8'
            a.collected[k] = a.tab
        return f
