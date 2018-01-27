class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQX$$1",
            "collections": [
                "DBORASQX"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, sqlid as label, execs as value from DBORASQX) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)