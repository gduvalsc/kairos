class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKRA$$1",
            "collections": [
                "NMONDISKREAD"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, id label, value / 1024.0 value from NMONDISKREAD) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)