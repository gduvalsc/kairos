class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHPHVRC",
            "collection": "ORAHQS",
            "request": "select h.timestamp timestamp, 'Captured PHVs' label, sum(disk_reads_delta * 1.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
