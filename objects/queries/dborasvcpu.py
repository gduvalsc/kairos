class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVCPU",
            "collection": "DBORASRV",
            "filterable": True,
            "request": "select timestamp, service label, sum(cpu) value from DBORASRV group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
