class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVPR",
            "collection": "DBORASRV",
            "filterable": True,
            "request": "select timestamp, service label, sum(1024 * reads) value from DBORASRV group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
