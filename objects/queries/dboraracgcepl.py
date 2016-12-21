class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACGCEPL",
            "collection": "DBORARACGCEP",
            "filterable": True,
            "request": "select timestamp, inum label, avg(plocal) value from DBORARACGCEP group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
