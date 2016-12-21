class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKOVW",
            "collection": "NMONDISKWRITE",
            "request": "select timestamp, 'Write MB/s' label, sum(value / 1024.0) value from NMONDISKWRITE group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
