class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARDBSY$$2",
            "collections": [
                "SARD"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Max (%) all disks' label, max(value) value from (select timestamp, 'xxx' label, busy value from SARD) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)