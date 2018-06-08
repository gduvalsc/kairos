class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKSVC$$1",
            "collections": [
                "NMONDISKSERV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, id as label, value as value from NMONDISKSERV) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)