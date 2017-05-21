class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQP$$1",
            "collections": [
                "DBORASQP"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sqlid label, parses value from DBORASQP) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)