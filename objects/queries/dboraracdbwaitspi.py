class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACDBWAITSPI",
            "collection": "DBORARACTTFE",
            "request": "select timestamp, inum label, sum(timewaited) value from DBORARACTTFE where inum!=0 and event != 'DB CPU' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
