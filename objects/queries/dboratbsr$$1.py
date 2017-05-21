class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORATBSR$$1",
            "collections": [
                "DBORATBS"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, tablespace label, reads value from DBORATBS) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)