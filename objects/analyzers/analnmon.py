class UserObject(dict):
    def __init__(s):
        object = {
            "type": "analyzer",
            "id": "ANALNMON",
            "begin": s.begin,
            "end": s.end,
            "rules": [],
            "contextrules": [
            ],
            "outcontextrules": [
                {"action": s.gettimestamp, "regexp": '^ZZZZ,(T\d+),(\d+):(\d+):(\d+),(\d+)-(\w+)-(\d+)'},
                {"action": s.getcpuval, "regexp": '^(CPU\d+),(T\d+),(.+?),(.+?),(.+?),(.+?)$', "scope": "NMONCPU"},
                {"action": s.getcpuall, "regexp": '^CPU_ALL,(T\d+),(.+?),(.+?),(.+?),(.+?),(.*?),(.+?)$', "scope": "NMONCPU"},
                {"action": s.genc2("NMONDISKBSIZE"), "regexp": '^DISKBSIZE([1-9]*),Disk .*?,(.+)$', "scope": "NMONDISKBSIZE"},
                {"action": s.genv2("NMONDISKBSIZE"), "regexp": '^DISKBSIZE([1-9]*),(T\d+),(.+)$', "scope": "NMONDISKBSIZE"},
                {"action": s.genc2("NMONDISKBUSY"), "regexp": '^DISKBUSY([1-9]*),Disk .*?,(.+)$', "scope": "NMONDISKBUSY"},
                {"action": s.genv2("NMONDISKBUSY"), "regexp": '^DISKBUSY([1-9]*),(T\d+),(.+)$', "scope": "NMONDISKBUSY"},
                {"action": s.genc2("NMONDISKREAD"), "regexp": '^DISKREAD([1-9]*),Disk .*?,(.+)$', "scope": "NMONDISKREAD"},
                {"action": s.genv2("NMONDISKREAD"), "regexp": '^DISKREAD([1-9]*),(T\d+),(.+)$', "scope": "NMONDISKREAD"},
                {"action": s.genc2("NMONDISKSERV"), "regexp": '^DISKSERV([1-9]*),Disk .*?,(.+)$', "scope": "NMONDISKSERV"},
                {"action": s.genv2("NMONDISKSERV"), "regexp": '^DISKSERV([1-9]*),(T\d+),(.+)$', "scope": "NMONDISKSERV"},
                {"action": s.genc2("NMONDISKWAIT"), "regexp": '^DISKWAIT([1-9]*),Disk .*?,(.+)$', "scope": "NMONDISKWAIT"},
                {"action": s.genc2("NMONDISKWAIT"), "regexp": '^DISKWAIT([1-9]*),Average .*?,(.+)$', "scope": "NMONDISKWAIT"},
                {"action": s.genv2("NMONDISKWAIT"), "regexp": '^DISKWAIT([1-9]*),(T\d+),(.+)$', "scope": "NMONDISKWAIT"},
                {"action": s.genc2("NMONDISKWRITE"), "regexp": '^DISKWRITE([1-9]*),Disk .*?,(.+)$', "scope": "NMONDISKWRITE"},
                {"action": s.genv2("NMONDISKWRITE"), "regexp": '^DISKWRITE([1-9]*),(T\d+),(.+)$', "scope": "NMONDISKWRITE"},
                {"action": s.genc2("NMONDISKXFER"), "regexp": '^DISKXFER([1-9]*),Disk .*?,(.+)$', "scope": "NMONDISKXFER"},
                {"action": s.genv2("NMONDISKXFER"), "regexp": '^DISKXFER([1-9]*),(T\d+),(.+)$', "scope": "NMONDISKXFER"},
                {"action": s.genc2("NMONDISKRIO"), "regexp": '^DISKRIO([1-9]*),Disk .*?,(.+)$', "scope": "NMONDISKRIO"},
                {"action": s.genv2("NMONDISKRIO"), "regexp": '^DISKRIO([1-9]*),(T\d+),(.+)$', "scope": "NMONDISKRIO"},
                {"action": s.genc2("NMONDISKWIO"), "regexp": '^DISKWIO([1-9]*),Disk .*?,(.+)$', "scope": "NMONDISKWIO"},
                {"action": s.genv2("NMONDISKWIO"), "regexp": '^DISKWIO([1-9]*),(T\d+),(.+)$', "scope": "NMONDISKWIO"},
                {"action": s.genc1("NMONDGBUSY"), "regexp": '^DGBUSY,Disk .*?,(.+)$', "scope": "NMONDGBUSY"},
                {"action": s.genv1("NMONDGBUSY"), "regexp": '^DGBUSY,(T\d+),(.+)$', "scope": "NMONDGBUSY"},
                {"action": s.genc1("NMONDGREAD"), "regexp": '^DGREAD,Disk .*?,(.+)$', "scope": "NMONDGREAD"},
                {"action": s.genv1("NMONDGREAD"), "regexp": '^DGREAD,(T\d+),(.+)$', "scope": "NMONDGREAD"},
                {"action": s.genc1("NMONDGWRITE"), "regexp": '^DGWRITE,Disk .*?,(.+)$', "scope": "NMONDGWRITE"},
                {"action": s.genv1("NMONDGWRITE"), "regexp": '^DGWRITE,(T\d+),(.+)$', "scope": "NMONDGWRITE"},
                {"action": s.genc1("NMONDGXFER"), "regexp": '^DGXFER,Disk .*?,(.+)$', "scope": "NMONDGXFER"},
                {"action": s.genv1("NMONDGXFER"), "regexp": '^DGXFER,(T\d+),(.+)$', "scope": "NMONDGXFER"},
                {"action": s.genc1("NMONDGSIZE"), "regexp": '^DGSIZE,Disk .*?,(.+)$', "scope": "NMONDGSIZE"},
                {"action": s.genv1("NMONDGSIZE"), "regexp": '^DGSIZE,(T\d+),(.+)$', "scope": "NMONDGSIZE"},
                {"action": s.genc1("NMONFILE"), "regexp": '^FILE,File .*?,(.+)$', "scope": "NMONFILE"},
                {"action": s.genv1("NMONFILE"), "regexp": '^FILE,(T\d+),(.+)$', "scope": "NMONFILE"},
                {"action": s.genc1("NMONIOADAPT"), "regexp": '^IOADAPT,Disk .*?,(.+)$', "scope": "NMONIOADAPT"},
                {"action": s.genv1("NMONIOADAPT"), "regexp": '^IOADAPT,(T\d+),(.+)$', "scope": "NMONIOADAPT"},
                {"action": s.genc1("NMONJFSFILE"), "regexp": '^JFSFILE,JFS .*?,(.+)$', "scope": "NMONJFSFILE"},
                {"action": s.genv1("NMONJFSFILE"), "regexp": '^JFSFILE,(T\d+),(.+)$', "scope": "NMONJFSFILE"},
                {"action": s.genc1("NMONJFSINODE"), "regexp": '^JFSINODE,JFS .*?,(.+)$', "scope": "NMONJFSINODE"},
                {"action": s.genv1("NMONJFSINODE"), "regexp": '^JFSINODE,(T\d+),(.+)$', "scope": "NMONJFSINODE"},
                {"action": s.genc1("NMONLARGEPAGE"), "regexp": '^LARGEPAGE,Large Page .*?,(.+)$', "scope": "NMONLARGEPAGE"},
                {"action": s.genv1("NMONLARGEPAGE"), "regexp": '^LARGEPAGE,(T\d+),(.+)$', "scope": "NMONLARGEPAGE"},
                {"action": s.genc1("NMONLPAR"), "regexp": '^LPAR,Logical Partition .*?,(.+)$', "scope": "NMONLPAR"},
                {"action": s.genc1("NMONLPAR"), "regexp": '^LPAR,LPAR .*?,(.+)$', "scope": "NMONLPAR"},
                {"action": s.genv1("NMONLPAR"), "regexp": '^LPAR,(T\d+),(.+)$', "scope": "NMONLPAR"},
                {"action": s.genc1("NMONMEM"), "regexp": '^MEM,Memory.*?,(.+)$', "scope": "NMONMEM"},
                {"action": s.genv1("NMONMEM"), "regexp": '^MEM,(T\d+),(.+)$', "scope": "NMONMEM"},
                {"action": s.genc1("NMONMEMNEW"), "regexp": '^MEMNEW,Memory *New.*?,(.+)$', "scope": "NMONMEMNEW"},
                {"action": s.genv1("NMONMEMNEW"), "regexp": '^MEMNEW,(T\d+),(.+)$', "scope": "NMONMEMNEW"},
                {"action": s.genc1("NMONMEMUSE"), "regexp": '^MEMUSE,Memory *Use.*?,(.+)$', "scope": "NMONMEMUSE"},
                {"action": s.genv1("NMONMEMUSE"), "regexp": '^MEMUSE,(T\d+),(.+)$', "scope": "NMONMEMUSE"},
                {"action": s.genc1("NMONNET"), "regexp": '^NET,Network .*?,(.+)$', "scope": "NMONNET"},
                {"action": s.genv1("NMONNET"), "regexp": '^NET,(T\d+),(.+)$', "scope": "NMONNET"},
                {"action": s.genc1("NMONNETERROR"), "regexp": '^NETERROR,Network .*?,(.+)$', "scope": "NMONNETERROR"},
                {"action": s.genv1("NMONNETERROR"), "regexp": '^NETERROR,(T\d+),(.+)$', "scope": "NMONNETERROR"},
                {"action": s.genc1("NMONNETPACKET"), "regexp": '^NETPACKET,Network .*?,(.+)$', "scope": "NMONNETPACKET"},
                {"action": s.genv1("NMONNETPACKET"), "regexp": '^NETPACKET,(T\d+),(.+)$', "scope": "NMONNETPACKET"},
                {"action": s.genc1("NMONNETSIZE"), "regexp": '^NETSIZE,Network .*?,(.+)$', "scope": "NMONNETSIZE"},
                {"action": s.genv1("NMONNETSIZE"), "regexp": '^NETSIZE,(T\d+),(.+)$', "scope": "NMONNETSIZE"},
                {"action": s.genc1("NMONNFSCLIV2"), "regexp": '^NFSCLIV2,NFS Client .*?,(.+)$', "scope": "NMONNFSCLIV2"},
                {"action": s.genv1("NMONNFSCLIV2"), "regexp": '^NFSCLIV2,(T\d+),(.+)$', "scope": "NMONNFSCLIV2"},
                {"action": s.genc1("NMONNFSCLIV3"), "regexp": '^NFSCLIV3,NFS Client .*?,(.+)$', "scope": "NMONNFSCLIV3"},
                {"action": s.genv1("NMONNFSCLIV3"), "regexp": '^NFSCLIV3,(T\d+),(.+)$', "scope": "NMONNFSCLIV3"},
                {"action": s.genc1("NMONNFSSVRV2"), "regexp": '^NFSSVRV2,NFS Server .*?,(.+)$', "scope": "NMONNFSSVRV2"},
                {"action": s.genv1("NMONNFSSVRV2"), "regexp": '^NFSSVRV2,(T\d+),(.+)$', "scope": "NMONNFSSVRV2"},
                {"action": s.genc1("NMONNFSSVRV3"), "regexp": '^NFSSVRV3,NFS Server .*?,(.+)$', "scope": "NMONNFSSVRV3"},
                {"action": s.genv1("NMONNFSSVRV3"), "regexp": '^NFSSVRV3,(T\d+),(.+)$', "scope": "NMONNFSSVRV3"},
                {"action": s.genc1("NMONPAGE"), "regexp": '^PAGE,Paging .*?,(.+)$', "scope": "NMONPAGE"},
                {"action": s.genv1("NMONPAGE"), "regexp": '^PAGE,(T\d+),(.+)$', "scope": "NMONPAGE"},
                {"action": s.genc1("NMONPOOLS"), "regexp": '^POOLS,Multiple .*?,(.+)$', "scope": "NMONPOOLS"},
                {"action": s.genv1("NMONPOOLS"), "regexp": '^POOLS,(T\d+),(.+)$', "scope": "NMONPOOLS"},
                {"action": s.genc1("NMONPROC"), "regexp": '^PROC,Processes .*?,(.+)$', "scope": "NMONPROC"},
                {"action": s.genv1("NMONPROC"), "regexp": '^PROC,(T\d+),(.+)$', "scope": "NMONPROC"},
                {"action": s.genc1("NMONPROCAIO"), "regexp": '^PROCAIO,Asynchronous .*?,(.+)$', "scope": "NMONPROCAIO"},
                {"action": s.genv1("NMONPROCAIO"), "regexp": '^PROCAIO,(T\d+),(.+)$', "scope": "NMONPROCAIO"},
                {"action": s.genc1("NMONVM"), "regexp": '^VM,Paging .*?,(.+)$', "scope": "NMONVM"},
                {"action": s.genv1("NMONVM"), "regexp": '^VM,(T\d+),(.+)$', "scope": "NMONVM"},
                {"action": s.top, "regexp": '^TOP,.PID,Time,(.+)$', "scope": "NMONTOP"},
                {"action": s.topval, "regexp": '^TOP,([0-9]+),(T\d+),(.+)$', "scope": "NMONTOP"},
                {"action": s.aaa, "regexp": '^AAA,(.+?),(.+)$', "scope": "NMONAAA"},
            ]
        }
        super(UserObject, s).__init__(**object)

    def begin(s, a):
        def tof(x):
            try: r = float(x)
            except: r = float(0)
            if str(r) == 'inf': r = 0.0
            if str(r) == 'nan': r = 0.0
            return r
        a.tof = tof
        a.desc = dict()
        a.nmontimestamp = dict()
        a.month = dict(JAN='01', FEB='02', MAR='03', APR='04', MAY='05', JUN='06', JUL='07', AUG='08', SEP='09', OCT='10', NOV='11', DEC='12')

    def end(s, a):
        pass

    def gettimestamp(s, a, l, g, m):
        a.nmontimestamp[g(1)] = g(7) + a.month[g(6).upper()] + g(5) + g(2) + g(3) + g(4) + "000"

    def getcpuval(s, a, l, g, m):
        if "NMONCPU" not in a.desc: a.desc["NMONCPU"] = dict(timestamp='text', id='text', user='real', sys='real', wait='real', idle='real', busy='real', cpus='real')
        cpuid = int(g(1)[3:])
        a.emit("NMONCPU", a.desc["NMONCPU"], dict(timestamp = a.nmontimestamp[g(2)], id = cpuid, user = a.tof(g(3)), sys = a.tof(g(4)), wait = a.tof(g(5)), idle = a.tof(g(6)), busy = 0.0, cpus = 1.0))

    def getcpuall(s, a, l, g, m):
        if "NMONCPU" not in a.desc: a.desc["NMONCPU"] = dict(timestamp='text', id='text', user='real', sys='real', wait='real', idle='real', busy='real', cpus='real')
        cpuid='ALL'
        a.emit("NMONCPU", a.desc["NMONCPU"], dict(timestamp = a.nmontimestamp[g(1)], id = cpuid, user = a.tof(g(2)), sys = a.tof(g(3)), wait = a.tof(g(4)), idle = a.tof(g(5)), busy = a.tof(g(6)), cpus = a.tof(g(7))))

    def genc1(s, table):
        def f(a, l ,g, m):
            setattr(a, table.lower(), g(1).split(','))
            if table not in a.desc: a.desc[table] = dict(timestamp = 'text', id = 'text', value = 'real')
        return f

    def genv1(s, table):
        def f(a, l ,g, m):
            val=g(2).split(',')
            for i in range(len(val)): a.emit(table, a.desc[table], dict(timestamp = a.nmontimestamp[g(1)], id = getattr(a, table.lower())[i], value = a.tof(val[i])))
        return f

    def genc2(s, table):
        def f(a, l ,g, m):
            i = g(1) if g(1) else 0
            if not hasattr(a, table.lower()): setattr(a, table.lower(), {})
            getattr(a, table.lower())[i] = g(2).split(',')
            if table not in a.desc: a.desc[table] = dict(timestamp = 'text', id = 'text', value = 'real')
        return f

    def genv2(s, table):
        def f(a, l ,g, m):
            i = g(1) if g(1) else 0
            val = g(3).split(',')
            for j in range(len(val)): a.emit(table, a.desc[table], dict(timestamp = a.nmontimestamp[g(2)], id = getattr(a,table.lower())[i][j], value = a.tof(val[j])))
        return f

    def top(s, a, l, g, m):
        setattr(a, 'nmontop', g(1).split(','))
        a.desc['NMONTOP'] = dict(timestamp = 'text', process = 'text', id = 'text', value = 'text')

    def topval(s, a, l, g, m):
        val = g(3).split(',')
        for i in range(len(val)): a.emit('NMONTOP', a.desc['NMONTOP'], dict(timestamp = a.nmontimestamp[g(2)], process = g(1), id = getattr(a, 'nmontop')[i], value = val[i]))

    def aaa(s, a, l, g, m):
        if 'NMONAAA' not in a.desc: a.desc['NMONAAA'] = dict(id = 'text', value = 'text')
        a.emit('NMONAAA', a.desc['NMONAAA'], dict(id = g(1), value = g(2)))
