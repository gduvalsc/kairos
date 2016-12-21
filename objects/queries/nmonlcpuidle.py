class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONLCPUIDLE",
            "collection": "NMONCPU",
            "filterable": True,
            "request": "select timestamp, 'CPU'||id label, sum(idle / 100.0) value from NMONCPU group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
