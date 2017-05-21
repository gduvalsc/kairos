class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORATBSW$$1",
            "collections": [
                "DBORATBS"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, tablespace label, writes value from DBORATBS) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)