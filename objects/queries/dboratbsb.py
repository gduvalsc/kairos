class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORATBSB",
            "collection": "DBORATBS",
            "filterable": True,
            "request": "select timestamp, tablespace label, sum(busytime * busy / 1000.0) value from DBORATBS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
