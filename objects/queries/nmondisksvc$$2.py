class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKSVC$$2",
            "collections": [
                "NMONDISKSERV"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Max service time' label, max(value) value from (select timestamp, 'xxx' label, value value from NMONDISKSERV) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)