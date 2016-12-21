class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSGC",
            "collection": "ORAHQS",
            "request": "select h.timestamp timestamp, 'Captured FMSs' label, sum(buffer_gets_delta * 1.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
