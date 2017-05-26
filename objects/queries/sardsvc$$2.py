class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARDSVC$$2",
            "collections": [
                "SARD"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Max service time (all disks)' label, max(value) value from (select timestamp, 'xxx' label, avserv value from SARD) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)