class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQW$$1",
            "collections": [
                "DBORASQW"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, sqlid as label, clusterwait as value from DBORASQW) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)