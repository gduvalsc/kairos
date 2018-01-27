class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKSVC$$2",
            "collections": [
                "NMONDISKSERV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, max(value) as value from (select timestamp, 'Max service time'::text as label, value as value from NMONDISKSERV) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)