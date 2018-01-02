class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQV$$1",
            "collections": [
                "DBORASQV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, sqlid as label, versioncount as value from DBORASQV) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)