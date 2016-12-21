class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACDBCPUPI",
            "collection": "DBORARACTM",
            "filterable": True,
            "request": "select timestamp, inum label, sum(dbcpu) value from DBORARACTM group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
