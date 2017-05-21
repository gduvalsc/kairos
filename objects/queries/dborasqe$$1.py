class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQE$$1",
            "collections": [
                "DBORASQE"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sqlid label, elapsed value from DBORASQE) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)