class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKSVC",
            "collection": "NMONDISKSERV",
            "filterable": True,
            "request": "select timestamp, id label, avg(value) value from NMONDISKSERV group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
