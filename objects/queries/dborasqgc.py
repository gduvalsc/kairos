class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQGC",
            "collection": "DBORASQG",
            "request": "select timestamp, 'Captured SQLs' label, sum(gets) value from DBORASQG group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
