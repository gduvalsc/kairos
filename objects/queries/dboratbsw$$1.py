class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORATBSW$$1",
            "collections": [
                "DBORATBS"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, tablespace as label, writes as value from DBORATBS) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)