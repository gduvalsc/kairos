class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQMC",
            "collection": "DBORASQM",
            "request": "select timestamp, 'Captured SQLs' label, sum(sharedmem) value from DBORASQM group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
