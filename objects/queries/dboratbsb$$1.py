class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORATBSB$$1",
            "collections": [
                "DBORATBS"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, tablespace label, busytime * busy / 1000.0 value from DBORATBS) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)