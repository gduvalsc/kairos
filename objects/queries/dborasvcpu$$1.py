class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVCPU$$1",
            "collections": [
                "DBORASRV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, service as label, cpu as value from DBORASRV) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)