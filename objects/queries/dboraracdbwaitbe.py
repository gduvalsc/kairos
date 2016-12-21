class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACDBWAITBE",
            "collection": "DBORARACTTBE",
            "request": "select timestamp, 'All background events' label, sum(timewaited) value from DBORARACTTBE where inum=0 and event != 'DB CPU' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
