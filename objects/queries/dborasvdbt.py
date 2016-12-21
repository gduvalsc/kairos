class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVDBT",
            "collection": "DBORASRV",
            "filterable": True,
            "request": "select timestamp, service label, sum(dbtime) value from DBORASRV group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
