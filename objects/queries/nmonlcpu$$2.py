class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONLCPU$$2",
            "collections": [
                "NMONCPU"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'Logical CPU' label, (user + sys) / 100.0 value from NMONCPU) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)