class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSWRC",
            "collection": "ORAHQS",
            "request": "select h.timestamp timestamp, 'Captured FMSs' label, sum(clwait_delta / 1000000.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
