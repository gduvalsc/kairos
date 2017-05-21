class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQV$$1",
            "collections": [
                "DBORASQV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sqlid label, versioncount value from DBORASQV) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)