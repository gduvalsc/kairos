class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAFILB$$1",
            "collections": [
                "DBORAFIL"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, file label, busytime * busy / 1000.0 value from DBORAFIL) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)