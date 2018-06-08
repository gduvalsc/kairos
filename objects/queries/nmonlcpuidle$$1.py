class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONLCPUIDLE$$1",
            "collections": [
                "NMONCPU"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'CPU'::text||id as label, (idle) / 100.0 as value from NMONCPU) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)