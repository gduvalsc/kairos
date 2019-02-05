import logging
class UserObject(dict):
    def __init__(s):
        object = {
            "type": "analyzer",
            "id": "ANALSNAPPER",
            "begin": s.begin,
            "end": s.end,
            "rules": [
                {"action": s.asummary, "regexp": 'End of ASH snap.+end=(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2}).+AAS=([\d\.\,]+)$'},
            ],
            "contextrules": [
                {"action": s.adata_old, "context": "old", "regexp": '\((\d+)\%\) +\| +(.*?) +\| +(.*?) +\| +(\d*) +\| +(\w*) +\| +(\d*) +\| +(.*) *$'},
                {"action": s.adata, "context": "new", "regexp": '\((\d+)\%\) +\| +(.*?) +\| +(.*?) +\| +(\d*) +\| +(\w*) +\| +(\d*) +\| +(.*?) +\| (\d*) *$'},
            ],
            "outcontextrules": [
                {"action": s.aheader2, "regexp": 'ActSes +%Thread.+EVENT *$'},
                {"action": s.aheader1, "regexp": 'ActSes +%Thread.+COMMAND *$'},
                {"action": s.aheader0, "regexp": 'No active sessions captured during the sampling period'},
            ]
        }
        super(UserObject, s).__init__(**object)

    def begin(s, a):
        a.desctable = dict(timestamp='text', pthread='real', aas='real', program='text', sid='text', username='text', sql_id='text', sql_child='text', event='text', command='text')
        a.data = []
        
    def aheader2(s, a, l ,g, m):
        a.data = []
        a.setContext('old')
        
    def aheader1(s, a, l ,g, m):
        a.data = []
        a.setContext('new')
        
    def aheader0(s, a, l ,g, m):
        a.data = []
        a.setContext('')

    def end(s, a):
        pass
    
    def adata_old(s, a, l ,g, m):
        d = dict(pthread=g(1), program=g(2), username=g(3), sid=g(4), sql_id=g(5), sql_child=g(6), event=g(7), command='')
        a.data.append(d)
    
    def adata(s, a, l ,g, m):
        d = dict(pthread=g(1), program=g(2), username=g(3), sid=g(4), sql_id=g(5), sql_child=g(6), event=g(7), command=g(8))
        a.data.append(d)

    def asummary(s, a, l ,g, m):
        timestamp = g(1) + g(2) + g(3) + g(4) + g(5) + g(6) + '000'
        aas = g(7).replace(',', '.')
        stack = []
        for r in a.data:
            r['timestamp'] = timestamp
            r['aas'] = aas
            stack.append(r)
        a.setContext('')
        a.emit("SNAPPER", a.desctable, stack)