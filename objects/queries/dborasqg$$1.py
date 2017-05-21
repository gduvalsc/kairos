class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQG$$1",
            "collections": [
                "DBORASQG"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sqlid label, gets value from DBORASQG) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)