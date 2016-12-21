class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAFILB",
            "collection": "DBORAFIL",
            "filterable": True,
            "request": "select timestamp, file label, sum(busytime * busy / 1000.0) value from DBORAFIL group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
