class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQM$$1",
            "collections": [
                "DBORASQM"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sqlid label, sharedmem value from DBORASQM) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)