class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKOV$$1",
            "collections": [
                "NMONDISKREAD"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Read MB/s' label, sum(value) value from (select timestamp, 'xxx' label, value / 1024.0 value from NMONDISKREAD) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)