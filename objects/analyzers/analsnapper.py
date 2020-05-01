import logging
class UserObject(dict):
    def __init__(self):
        object = {
            "type": "analyzer",
            "id": "ANALSNAPPER",
            "begin": self.begin,
            "end": self.end,
            "rules": [
                {"action": self.asummary, "regexp": r'End of ASH snap.+end=(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2}).+AAS=([\d\.\,]+)$'},
            ],
            "contextrules": [
                {"action": self.adata_old, "context": "old", "regexp": r'\((\d+)\%\) +\| +(.*?) +\| +(.*?) +\| +(\d*) +\| +(\w*) +\| +(\d*) +\| +(.*) *$'},
                {"action": self.adata, "context": "new", "regexp": r'\((\d+)\%\) +\| +(.*?) +\| +(.*?) +\| +(\d*) +\| +(\w*) +\| +(\d*) +\| +(.*?) +\| (\d*) *$'},
            ],
            "outcontextrules": [
                {"action": self.aheader2, "regexp": r'ActSes +%Thread.+EVENT *$'},
                {"action": self.aheader1, "regexp": r'ActSes +%Thread.+COMMAND *$'},
                {"action": self.aheader0, "regexp": r'No active sessions captured during the sampling period'},
            ]
        }
        super(UserObject, self).__init__(**object)

    def begin(self, a):
        a.desctable = dict(timestamp='text', pthread='real', aas='real', program='text', sid='text', username='text', sql_id='text', sql_child='text', event='text', command='text')
        a.data = []
        
    def aheader2(self, a, l ,g, m):
        a.data = []
        a.setContext('old')
        
    def aheader1(self, a, l ,g, m):
        a.data = []
        a.setContext('new')
        
    def aheader0(self, a, l ,g, m):
        a.data = []
        a.setContext('')

    def end(self, a):
        pass
    
    def adata_old(self, a, l ,g, m):
        d = dict(pthread=g(1), program=g(2), username=g(3), sid=g(4), sql_id=g(5), sql_child=g(6), event=g(7), command='')
        a.data.append(d)
    
    def adata(self, a, l ,g, m):
        d = dict(pthread=g(1), program=g(2), username=g(3), sid=g(4), sql_id=g(5), sql_child=g(6), event=g(7), command=g(8))
        a.data.append(d)

    def asummary(self, a, l ,g, m):
        timestamp = g(1) + g(2) + g(3) + g(4) + g(5) + g(6) + '000'
        aas = g(7).replace(',', '.')
        stack = []
        for r in a.data:
            r['timestamp'] = timestamp
            r['aas'] = aas
            stack.append(r)
        a.setContext('')
        a.emit("SNAPPER", a.desctable, stack)