class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACGCEPD",
            "collection": "DBORARACGCEP",
            "filterable": True,
            "request": "select timestamp, inum label, avg(pdisk) value from DBORARACGCEP group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
