class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONLCPUIDLE$$2",
            "collections": [
                "NMONCPU"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'Idle logical CPU' label, (idle) / 100.0 value from NMONCPU) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)