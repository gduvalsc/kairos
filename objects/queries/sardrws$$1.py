class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARDRWS$$1",
            "collections": [
                "SARD"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, device as label, rws as value from SARD) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)