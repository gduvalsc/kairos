class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACDBWAITBEPEI",
            "collection": "DBORARACTTBE",
            "filterable": True,
            "request": "select timestamp, event||' / '||inum label, sum(timewaited) value from DBORARACTTBE where inum!=0 and event != 'DB CPU' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
