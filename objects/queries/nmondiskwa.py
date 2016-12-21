class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKWA",
            "collection": "NMONDISKWRITE",
            "filterable": True,
            "request": "select timestamp, id label, sum(value / 1024.0) value from NMONDISKWRITE group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
