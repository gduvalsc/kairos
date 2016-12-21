class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQCC",
            "collection": "DBORASQC",
            "request": "select timestamp, 'Captured SQLs' label, sum(cpu) value from DBORASQC group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
