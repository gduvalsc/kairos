class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONSYS",
            "collection": "NMONPROC",
            "request": "select timestamp, id label, sum(value) value from NMONPROC group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
