class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQC$$1",
            "collections": [
                "DBORASQC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sqlid label, cpu value from DBORASQC) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)