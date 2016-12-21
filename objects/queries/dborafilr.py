class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAFILR",
            "collection": "DBORAFIL",
            "filterable": True,
            "request": "select timestamp, file label, sum(reads) value from DBORAFIL group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
