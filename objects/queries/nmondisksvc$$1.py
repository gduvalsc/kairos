class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKSVC$$1",
            "collections": [
                "NMONDISKSERV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, avg(value) value from (select timestamp, id label, value value from NMONDISKSERV) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)