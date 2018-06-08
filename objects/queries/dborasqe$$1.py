class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQE$$1",
            "collections": [
                "DBORASQE"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, sqlid as label, elapsed as value from DBORASQE) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)