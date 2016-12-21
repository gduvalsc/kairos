class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACDBTIME",
            "collection": "DBORARACTM",
            "request": "select timestamp, 'DB time' label, sum(dbtime) value from DBORARACTM group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
