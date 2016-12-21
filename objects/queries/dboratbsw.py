class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORATBSW",
            "collection": "DBORATBS",
            "filterable": True,
            "request": "select timestamp, tablespace label, sum(writes) value from DBORATBS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
