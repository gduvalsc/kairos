class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARDRWS$$2",
            "collections": [
                "SARD"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Max throughput (all disks)' label, max(value) value from (select timestamp, 'xxx' label, rws value from SARD) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)