class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONMEMUSE",
            "collection": "NMONMEMNEW",
            "request": "select timestamp, id label, sum(value) value from NMONMEMNEW where id in ('Process%','System%','FScache%','Free%') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
