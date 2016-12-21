class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKBSY",
            "collection": "NMONDISKBUSY",
            "filterable": True,
            "request": "select timestamp, id label, avg(value) value from NMONDISKBUSY group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
