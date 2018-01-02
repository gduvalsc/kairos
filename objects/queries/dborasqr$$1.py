class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQR$$1",
            "collections": [
                "DBORASQR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, sqlid as label, reads as value from DBORASQR) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)