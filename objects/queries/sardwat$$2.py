class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARDWAT$$2",
            "collections": [
                "SARD"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, max(value) as value from (select timestamp, 'Max wait time (all disks)'::text as label, avwait as value from SARD) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)