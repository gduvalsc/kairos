class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAFILW$$1",
            "collections": [
                "DBORAFIL"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, file as label, writes as value from DBORAFIL) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)