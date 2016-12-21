class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQPC",
            "collection": "DBORASQP",
            "request": "select timestamp, 'Captured SQLs' label, sum(parses) value from DBORASQP group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
