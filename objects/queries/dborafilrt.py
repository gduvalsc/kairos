class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAFILRT",
            "collection": "DBORAFIL",
            "filterable": True,
            "request": "select timestamp, file label, sum(readtime * reads / 1000.0) value from DBORAFIL group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
