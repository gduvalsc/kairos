class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONLCPUIDLEALL",
            "collection": "NMONCPU",
            "request": "select timestamp, 'Logical CPU' label, sum(idle / 100.0) value from NMONCPU group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
