class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQM$$1",
            "collections": [
                "DBORASQM"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, sqlid as label, sharedmem as value from DBORASQM) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)