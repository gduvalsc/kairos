class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACDBCPU",
            "collection": "DBORARACTM",
            "request": "select timestamp, 'DB CPU' label, sum(dbcpu) value from DBORARACTM group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
