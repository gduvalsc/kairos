class UserObject(dict):
    def __init__(s):
        object = {
            "type": "analyzer",
            "id": "ANALMAIN",
            "begin": s.begin,
            "end": s.end,
            "outcontextrules": [],
            "contextrules": [
                {"context": "gentype", "action": s.gentype, "regexp": '^\w+\s(\w+)\s+'}
            ],
            "rules": [
                {"action": s.awr, "regexp": '^WORKLOAD REPOSITORY report for'},
                {"action": s.astatspack, "regexp": '(^STATSPACK Statistics Report for|^STATSPACK report for)'},
                {"action": s.ebs, "regexp": '^REPORT TYPE: EBS12CM'},
                {"action": s.bo, "regexp": '^REPORT TYPE: BO'},
                {"action": s.gen, "regexp": '^REPORT TYPE: (\w+) '},
                {"action": s.json, "regexp": '^\s+"collection":\s*"(\w+)'},
                {"action": s.awrhtml, "regexp": '.[Hh][Ee][Aa][Dd].<[Tt][Ii][Tt][Ll][Ee]>AWR Report for DB:'},
                {"action": s.nmon, "regexp": '^AAA,progname,'},
                {"action": s.nmon, "regexp": '^CPU_ALL,'},
                {"action": s.awrrachtml, "regexp": '.head.<title>AWR RAC Report for DB:'},
                {"action": s.vmstat, "regexp": 'Collection Module:.+VmstatExaWatcher'},
                {"action": s.tthtml, "regexp": '.<[Tt][Ii][Tt][Ll][Ee]>TTSTATS REPORT'},
                {"action": s.sar, "regexp": '^(AIX|SunOS|HP-UX|Linux)[ \t]+(.+?)[ \t]+.*[ \t]+[0-9][0-9]/[0-9][0-9]/2?0?[0-9][0-9].*$'},
                {"action": s.snapper, "regexp": '^ +ActSes +%Thread'},
                {"action": s.snapper, "regexp": 'No active sessions captured during the sampling period'},
                {"action": s.stop, "regexp": '^'}
            ]
        }
        super(UserObject, s).__init__(**object)

    def begin(s, a):
        a.cpt = 0

    def end(s, a):
        pass

    def awr(s, a, l ,g, m):
        a.setContext('BREAK')
        a.emit(None, None, {
            "member": m,
            "analyzer": "ANALAWR",
            "collections": ['DBORAAWR', 'DBORAINFO', 'DBORAMISC', 'DBORAMDC', 'DBORADRV', 'DBORAWEC', 'DBORAWEV', 'DBORAWEB', 'DBORASTA', 'DBORAMTT', 'DBORALIB', 'DBORASQE', 'DBORASQP', 'DBORASQM', 'DBORASQV', 'DBORASQW', 'DBORASQG', 'DBORASQR', 'DBORASQX', 'DBORASQC', 'DBORAREQ', 'DBORALAT', 'DBORALAW', 'DBORAENQ', 'DBORATBS', 'DBORAFIL', 'DBORASGA', 'DBORAPGA', 'DBORAPGB', 'DBORAPGC', 'DBORAOSS', 'DBORATMS', 'DBORASRV', 'DBORASVW', 'DBORABUF', 'DBORASGLR', 'DBORASGPR', 'DBORASGPRR', 'DBORASGUR', 'DBORASGOR', 'DBORASGDPR', 'DBORASGPW', 'DBORASGPWR', 'DBORASGDPW', 'DBORASGTS', 'DBORASGDBC', 'DBORASGRLW', 'DBORASGIW', 'DBORASGBBW', 'DBORASGGCBB', 'DBORASGCRBR', 'DBORASGCBR']
        })

    def astatspack(s, a, l ,g, m):
        a.setContext('BREAK')
        a.emit(None, None, {
            "member": m,
            "analyzer": "ANALSP",
            "collections": ['DBORASTATSPACK', 'DBORAINFO', 'DBORAMISC', 'DBORAMDC', 'DBORADRV', 'DBORAWEC', 'DBORAWEV', 'DBORAWEB', 'DBORASTA', 'DBORAMTT', 'DBORALIB', 'DBORASQE', 'DBORASQP', 'DBORASQM', 'DBORASQV', 'DBORASQW', 'DBORASQG', 'DBORASQR', 'DBORASQX', 'DBORASQC', 'DBORAREQ', 'DBORALAT', 'DBORALAW', 'DBORAENQ', 'DBORATBS', 'DBORAFIL', 'DBORASGA', 'DBORAPGA', 'DBORAPGB', 'DBORAPGC', 'DBORAOSS', 'DBORATMS', 'DBORASRV', 'DBORASVW', 'DBORABUF', 'DBORASGLR', 'DBORASGPR', 'DBORASGPRR', 'DBORASGUR', 'DBORASGOR', 'DBORASGDPR', 'DBORASGPW', 'DBORASGPWR', 'DBORASGDPW', 'DBORASGTS', 'DBORASGDBC', 'DBORASGRLW', 'DBORASGIW', 'DBORASGBBW', 'DBORASGGCBB', 'DBORASGCRBR', 'DBORASGCBR']
        })

    def tthtml(s, a, l ,g, m):
        a.setContext('BREAK')
        a.emit(None, None, {
            "member": m,
            "analyzer": "ANALTTHTML",
            "collections": ['TTMISC', 'TTSTATS', 'TTPARAM', 'TTSQLTOPP', 'TTSQLTOPX', 'TTSQLTEXT', 'TTABSMETRICS', 'TTMETRICS']
        })

    def awrhtml(s, a, l, g, m):
        a.setContext('BREAK')
        a.emit(None, None, {
            "member": m,
            "analyzer": 'ANALAWRHTML',
            "collections": ['DBORAAWR', 'DBORAINFO', 'DBORAMISC', 'DBORAMDC', 'DBORABPA', 'DBORAWEC', 'DBORAWEV', 'DBORAWEB', 'DBORASTA', 'DBORAMTT', 'DBORALIB', 'DBORASQE', 'DBORASQP', 'DBORASQM', 'DBORASQV', 'DBORASQW', 'DBORASQG', 'DBORASQR', 'DBORASQX', 'DBORASQC', 'DBORAREQ', 'DBORALAT', 'DBORALAW', 'DBORAENQ', 'DBORATBS', 'DBORAFIL', 'DBORASGA', 'DBORAPGA', 'DBORAPGB', 'DBORAPGC', 'DBORAOSS', 'DBORATMS', 'DBORASRV', 'DBORASVW', 'DBORABUF', 'DBORASGLR', 'DBORASGPR', 'DBORASGPRR', 'DBORASGUR', 'DBORASGOR', 'DBORASGDPR', 'DBORASGPW', 'DBORASGPWR', 'DBORASGDPW', 'DBORASGTS', 'DBORASGDBC', 'DBORASGRLW', 'DBORASGIW', 'DBORASGBBW', 'DBORASGGCBB', 'DBORASGCRBR', 'DBORASGCBR', 'EXACPU', 'EXATOPDBIOR', 'EXATOPDBIOV', 'EXATOPDSKIOR', 'EXATOPDSKIOV', 'EXATOPCLLOSIO', 'EXATOPCLLOSIOL', 'EXATOPDSKOSIO', 'EXATOPDSKOSIOL']
        })
        
    def vmstat(s, a, l, g, m):
        a.setContext('BREAK')
        a.emit(None, None, {
            "member": m,
            "analyzer": 'ANALVMSTAT',
            "collections": ['VMSTAT']
        })
        
    def snapper(s, a, l, g, m):
        a.setContext('BREAK')
        a.emit(None, None, {
            "member": m,
            "analyzer": 'ANALSNAPPER',
            "collections": ['SNAPPER']
        })

    def awrrachtml(s, a, l, g, m):
        a.setContext('BREAK');
        a.emit(None, None, {
            "member": m,
            "analyzer": 'ANALAWRRACHTML',
            "collections": ['DBORARACMISC', 'DBORARACCSIZE', 'DBORARACOSS', 'DBORARACTM', 'DBORARACFWC', 'DBORARACTTE', 'DBORARACTTFE', 'DBORARACTTBE', 'DBORARACGALPSS', 'DBORARACGALPGM', 'DBORARACGCEP', 'DBORARACGCTS', 'DBORARACSTA', 'DBORARACSTAA', 'DBORARACSEG', 'DBORARACPING', 'DBORARACREQ', 'DBORARACSQE', 'DBORARACSQC', 'DBORARACSQI', 'DBORARACSQG', 'DBORARACSQR', 'DBORARACSQU', 'DBORARACSQX', 'DBORARACSQW']
        })

    def gen(s, a, l, g, m):
        a.setContext('gentype')

    def gentype(s, a, l, g, m):
        a.setContext('BREAK')
        a.emit(None, None, {
            "member": m,
            "analyzer": 'ANALGEN',
            "collections": [g(1)]
        })

    def json(s, a, l, g, m):
        a.setContext('BREAK')
        a.emit(None, None, {
            "member": m,
            "analyzer": 'ANALJSON',
            "collections": [g(1)]
        })

    def ebs(s, a, l, g, m):
        a.setContext('BREAK')
        a.emit(None, None, {
            "member": m,
            "analyzer": 'ANALEBS',
            "collections": ['EBS12CM']
        })

    def bo(s, a, l, g, m):
        a.setContext('BREAK')
        a.emit(None, None, {
            "member": m,
            "analyzer": 'ANALBO',
            "collections": ['BO']
        })

    def nmon(s, a, l ,g, m):
        a.setContext('BREAK')
        a.emit(None, None, {
            "member": m,
            "analyzer": "ANALNMON",
            "collections": ['NMONCPU', 'NMONDISKBSIZE', 'NMONDISKBUSY', 'NMONDISKREAD', 'NMONDISKSERV', 'NMONDISKWAIT', 'NMONDISKWRITE', 'NMONDISKXFER', 'NMONDISKRIO', 'NMONDISKWIO', 'NMONDGBUSY', 'NMONDGREAD', 'NMONDGWRITE', 'NMONDGXFER', 'NMONDGSIZE', 'NMONFILE', 'NMONIOADAPT', 'NMONJFSFILE', 'NMONJFSINODE', 'NMONLARGEPAGE', 'NMONLPAR', 'NMONMEM', 'NMONMEMNEW', 'NMONMEMUSE', 'NMONNET', 'NMONNETERROR', 'NMONNETPACKET', 'NMONNETSIZE', 'NMONNFSCLIV2', 'NMONNFSCLIV3', 'NMONNFSSVRV2', 'NMONNFSSVRV3', 'NMONPAGE', 'NMONPOOLS', 'NMONPROC', 'NMONPROCAIO', 'NMONVM', 'NMONTOP', 'NMONAAA']
        })

    def sar(s, a, l ,g, m):
        a.setContext('BREAK')
        a.emit(None, None, {
            "member": m,
            "analyzer": "ANALSAR",
            "collections": ['SARB', 'SARD', 'SARM', 'SARN', 'SARP', 'SARQ', 'SARU', 'SARV', 'SARW']
        })

    def stop(s, a, l, g, m):
        a.cpt += 1
        if (a.cpt > 9): a.setContext('BREAK')
