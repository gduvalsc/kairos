class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARDBSY$$2",
            "collections": [
                "SARD"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, max(value) as value from (select timestamp, 'Max (%) all disks'::text as label, busy as value from SARD) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)