class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQX$$1",
            "collections": [
                "DBORASQX"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sqlid label, execs value from DBORASQX) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)