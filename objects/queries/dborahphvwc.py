class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHPHVWC",
            "collection": "ORAHQS",
            "filterable": True,
            "request": "select h.timestamp timestamp, plan_hash_value label, sum(ccwait_delta / 1000000.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
