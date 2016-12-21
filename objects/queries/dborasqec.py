class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQEC",
            "collection": "DBORASQE",
            "request": "select timestamp, 'Captured SQLs' label, sum(elapsed) value from DBORASQE group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
