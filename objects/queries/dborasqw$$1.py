class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQW$$1",
            "collections": [
                "DBORASQW"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sqlid label, clusterwait value from DBORASQW) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)