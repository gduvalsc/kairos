class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQVC",
            "collection": "DBORASQV",
            "request": "select timestamp, 'Captured SQLs' label, sum(versioncount) value from DBORASQV group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
