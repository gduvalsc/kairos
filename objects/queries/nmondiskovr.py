class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKOVR",
            "collection": "NMONDISKREAD",
            "request": "select timestamp, 'Read MB/s' label, sum(value / 1024.0) value from NMONDISKREAD group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
