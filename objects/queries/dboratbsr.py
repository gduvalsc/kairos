class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORATBSR",
            "collection": "DBORATBS",
            "filterable": True,
            "request": "select timestamp, tablespace label, sum(reads) value from DBORATBS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
