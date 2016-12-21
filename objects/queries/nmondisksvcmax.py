class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKSVCMAX",
            "collection": "NMONDISKSERV",
            "filterable": True,
            "request": "select timestamp, 'Max service time' label, max(value) value from NMONDISKSERV group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
