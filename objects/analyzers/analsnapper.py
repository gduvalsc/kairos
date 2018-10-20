import logging
class UserObject(dict):
    def __init__(s):
        object = {
            "type": "analyzer",
            "id": "ANALSNAPPER",
            "begin": s.begin,
            "end": s.end,
            "rules": [
                {"action": s.aheader, "regexp": 'ActSes +%Thread'},
                {"action": s.adata, "regexp": '\((\d+)\%\) +\| +(.*?) +\| +(.*?) +\| +(\d*) +\| +(\w*) +\| +(\d*) +\| +(.*) *$'},
                {"action": s.asummary, "regexp": 'End of ASH snap.+end=(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2}).+AAS=([\d\.\,]+)$'},
            ],
            "contextrules": [],
            "outcontextrules": []
        }
        super(UserObject, s).__init__(**object)

    def begin(s, a):
        a.desctable = dict(timestamp='text', pthread='real', aas='real', program='text', sid='text', username='text', sql_id='text', sql_child='text', event='text')
        a.data = []
        
    def aheader(s, a, l ,g, m):
        a.data = []

    def end(s, a):
        pass
    
    def adata(s, a, l ,g, m):
        d = dict(pthread=g(1), program=g(2), username=g(3), sid=g(4), sql_id=g(5), sql_child=g(6), event=g(7))
        a.data.append(d)

    def asummary(s, a, l ,g, m):
        timestamp = g(1) + g(2) + g(3) + g(4) + g(5) + g(6) + '000'
        aas = g(7).replace(',', '.')
        stack = []
        for r in a.data:
            r['timestamp'] = timestamp
            r['aas'] = aas
            stack.append(r)
        a.emit("SNAPPER", a.desctable, stack)