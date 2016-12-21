class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGDPR",
            "collection": "DBORASGDPR",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(reads) value from DBORASGDPR group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
