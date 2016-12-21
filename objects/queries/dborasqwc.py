class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQWC",
            "collection": "DBORASQW",
            "request": "select timestamp, 'Captured SQLs' label, sum(clusterwait) value from DBORASQW group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
