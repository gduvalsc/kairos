import hashlib
class UserObject(dict):
    def __init__(s):
        object = {
            "type": "analyzer",
            "id": "ANALTTHTML",
            "content": "xml",
            "begin": s.begin,
            "end": s.end,
            "rules": [
                {"action": s.ah2, "regexp": '', "tag": 'h2'},
                {"action": s.atable, "regexp": '', "tag": 'table'},
                {"action": s.atr, "regexp": '', "tag": 'tr'},
                {"action": s.athd, "regexp": '', "tag": '(th|td)'}
            ],
            "contextrules": [
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsum"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thmuc", "scope": "TTABSMETRICS"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thlp", "scope": "TTMETRICS"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thss", "scope": "TTSTATS"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsqlp", "scope": "TTSQLTOPP"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsqlx", "scope": "TTSQLTOPX"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thsqlt"},
                {"action": s.athget, "regexp": '.', "tag": 'th', "context": "thprm", "scope": "TTPARAM"},
                {"action": s.atdget, "regexp": '.', "tag": 'td', "context": "tdsum"},
                {"action": s.atdget, "regexp": '.', "tag": 'td', "context": "tdmuc", "scope": "TTABSMETRICS"},
                {"action": s.atdget, "regexp": '.', "tag": 'td', "context": "tdlp", "scope": "TTMETRICS"},
                {"action": s.atdget, "regexp": '.', "tag": 'td', "context": "tdss", "scope": "TTSTATS"},
                {"action": s.atdget, "regexp": '.', "tag": 'td', "context": "tdsqlp", "scope": "TTSQLTOPP"},
                {"action": s.atdget, "regexp": '.', "tag": 'td', "context": "tdsqlx", "scope": "TTSQLTOPX"},
                {"action": s.atdget, "regexp": '.', "tag": 'td', "context": "tdsqlt"},
                {"action": s.atdget, "regexp": '.', "tag": 'td', "context": "tdprm", "scope": "TTPARAM"},
            ],
            "outcontextrules": [
                {"action": s.genstate('thsum'), "regexp": 'Summary', "tag": 'h2'},
                {"action": s.genstate('thss'), "regexp": 'Statement Statistics', "tag": 'h2', "scope": "TTSTATS"},
                {"action": s.genstate('thss'), "regexp": 'Transaction Statistics', "tag": 'h2', "scope": "TTSTATS"},
                {"action": s.genstate('thss'), "regexp": 'Log Statistics', "tag": 'h2', "scope": "TTSTATS"},
                {"action": s.genstate('thss'), "regexp": 'Checkpoint Statistics', "tag": 'h2', "scope": "TTSTATS"},
                {"action": s.genstate('thss'), "regexp": 'DB Activity Statistics', "tag": 'h2', "scope": "TTSTATS"},
                {"action": s.genstate('thss'), "regexp": 'Lock Statistics', "tag": 'h2', "scope": "TTSTATS"},
                {"action": s.genstate('thprm'), "regexp": 'Configuration Parameters', "tag": 'h2', "scope": "TTPARAM"},
                {"action": s.genstate('thsqlx'), "regexp": 'Executions% TotalCmd IDCmd Text', "tag": 'table', "scope": "TTSQLTOPX"},
                {"action": s.genstate('thsqlp'), "regexp": 'Preparations% TotalCmd IDCmd Text', "tag": 'table', "scope": "TTSQLTOPP"},
                {"action": s.genstate('thsqlt'), "regexp": 'SQL IDSQL Text', "tag": 'table', "scope": "TTSQLTEXT"},
                {"action": s.genstate('thsqlt'), "regexp": 'SQL IDSQL Text', "tag": 'table', "scope": "TTSQLTOPX"},
                {"action": s.genstate('thsqlt'), "regexp": 'SQL IDSQL Text', "tag": 'table', "scope": "TTSQLTOPP"},
                {"action": s.genstate('thmuc'), "regexp": 'MetricsBegin ValueEnd Value', "tag": 'table', "scope": "TTABSMETRICS"},
                {"action": s.genstate('thlp'), "regexp": 'MetricsPer SecondPer Transaction', "tag": 'table', "scope": "TTMETRICS"},
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
        convertid=dict()
        tof=lambda x: float(x.replace(',','').replace(u'\xa0','0')) if x!=u'' else 0.0
        toc=lambda x: x.replace('&quot;',"'").replace('&lt;',"<").replace('&gt;',">").replace(u'\xa0','')
        for x in sorted(a.collected.keys(),reverse=True):
            line=-1
            if x =='zz9':
                dttmisc = dict(timestamp='text', avgelapsed='real', elapsed='int')
                for y in a.collected[x]:
                    when = y['Info']
                    what = y['Snap Time']
                    if when == 'End Snap:':
                        year = str(what[0:4])
                        month = str(what[5:7])
                        day = str(what[8:10])
                        hour = str(what[11:13])
                        min = str(what[14:16])
                        sec = str(what[17:19])
                        a.date = year + month + day + hour + min + sec + "000"
                    if when == 'Elapsed Time:':
                        a.dur = int(tof(what[:-4]))
                        if 'TTMISC' in a.scope: a.emit('TTMISC', dttmisc, dict(timestamp=a.date, avgelapsed=float(a.dur), elapsed=int(a.dur)))
            if 'MetricsBegin ValueEnd Value' in x:
                d = dict(timestamp='text', metric='text', averagedvalue='real', summedvalue='int')
                for y in a.collected[x]:
                    metric = y['Metrics']
                    averagedvalue = tof(y['End Value'])
                    summedvalue = int(y['End Value'])
                    a.emit('TTABSMETRICS', d, dict(timestamp=a.date, metric=metric, averagedvalue=averagedvalue, summedvalue=summedvalue))
            if 'MetricsPer SecondPer Transaction' in x:
                d = dict(timestamp='text', metric='text', value='real')
                for y in a.collected[x]:
                    metric = y['Metrics']
                    value = tof(y['Per Second'])
                    a.emit('TTMETRICS', d, dict(timestamp=a.date, metric=metric, value=value))
            if 'Statement Statistics' in x or 'Transaction Statistics' in x or 'Log Statistics' in x or 'Checkpoint Statistics' in x or 'DB Activity Statistics' in x or 'Lock Statistics' in x:
                d = dict(timestamp='text', statistic='text', value='real')
                for y in a.collected[x]:
                    statistic = y['Statistics']
                    value = tof(y['Rate (Per Second)'])
                    a.emit('TTSTATS', d, dict(timestamp=a.date, statistic=statistic, value=value))
            if 'Preparations% TotalCmd IDCmd Text' in x:
                d = dict(timestamp='text', sqlid='text', hashid='text', prepares='real', percent='real')
                for y in a.collected[x]:
                    sqlid = y['Cmd ID']
                    hashid = convertid[sqlid]
                    prepares = tof(y['Preparations']) / a.dur
                    percent = tof(y['% Total'])
                    a.emit('TTSQLTOPP', d, dict(timestamp=a.date, sqlid=sqlid, hashid=hashid, prepares=prepares, percent=percent))
            if 'Executions% TotalCmd IDCmd Text' in x:
                d = dict(timestamp='text', sqlid='text', hashid='text', execs='real', percent='real')
                for y in a.collected[x]:
                    sqlid = y['Cmd ID']
                    hashid = convertid[sqlid]
                    execs = tof(y['Executions']) / a.dur
                    percent = tof(y['% Total'])
                    a.emit('TTSQLTOPX', d, dict(timestamp=a.date, sqlid=sqlid, hashid=hashid, execs=execs, percent=percent))
            if 'SQL IDSQL Text' in x:
                d = dict(sqlid='text', hashid='text', request='text')
                for y in a.collected[x]:
                    sqlid = y['SQL ID']
                    request = y['SQL Text']
                    convertid[sqlid] = hashlib.md5(request.encode()).hexdigest()
                    hashid = convertid[sqlid]
                    if 'TTSQLTEXT' in a.scope: a.emit('TTSQLTEXT', d, dict(sqlid=sqlid, hashid=hashid, request=request))
            if 'Configuration Parameters' in x:
                d = dict(parameter='text', begvalue='text', endvalue='text')
                for y in a.collected[x]:
                    parameter = y['Paramter']
                    begvalue = y['Begin Value']
                    endvalue = y['End Value']
                    a.emit('TTPARAM', d, dict(parameter=parameter, begvalue=begvalue, endvalue=endvalue))

    def ah2(s, a, l, g, m):
        context = ''
        a.setContext(context)
        if len(a.row): a.tab.append(a.row)
        a.row = {}
        a.cpt = -1
        a.collector = {}

    def atable(s, a, l, g, m):
        context = ''
        if a.reinit: a.setContext(context)
        if len(a.scope) < 3:
            if a.scope.issubset({'TTMISC'}) and 'zz9' in a.collected: a.setContext('BREAK')
            if a.scope.issubset({'TTPARAM'}) and 'Configuration Parameters' in a.collected and len(a.collected['Configuration Parameters']): a.setContext('BREAK')
            if a.scope.issubset({'TTABSMETRICS'}) and 'MetricsBegin ValueEnd Value' in a.collected and len(a.collected['MetricsBegin ValueEnd Value']): a.setContext('BREAK')
            if a.scope.issubset({'TTMETRICS'}) and 'MetricsPer SecondPer Transaction' in a.collected and len(a.collected['MetricsPer SecondPer Transaction']): a.setContext('BREAK')
            if a.scope.issubset({'TTSQLTOPP'}) and 'Preparations% TotalCmd IDCmd Text' in a.collected and len(a.collected['Preparations% TotalCmd IDCmd Text']): a.setContext('BREAK')
            if a.scope.issubset({'TTSQLTOPX'}) and 'Executions% TotalCmd IDCmd Text' in a.collected and len(a.collected['Executions% TotalCmd IDCmd Text']): a.setContext('BREAK')
            if a.scope.issubset({'TTSQLTEXT'}) and 'SQL IDSQL Text' in a.collected and len(a.collected['SQL IDSQL Text']): a.setContext('BREAK')
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
            if k == 'Summary': k = 'zz9'
            a.collected[k] = a.tab
        return f
