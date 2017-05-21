class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQR$$1",
            "collections": [
                "DBORASQR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sqlid label, reads value from DBORASQR) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)