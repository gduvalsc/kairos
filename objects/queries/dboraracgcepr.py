class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACGCEPR",
            "collection": "DBORARACGCEP",
            "filterable": True,
            "request": "select timestamp, inum label, avg(premote) value from DBORARACGCEP group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
