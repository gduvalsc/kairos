class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQM",
            "collection": "DBORASQM",
            "filterable": True,
            "request": "select timestamp, sqlid label, sum(sharedmem) value from DBORASQM group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
