class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGPR",
            "collection": "DBORASGPR",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(reads) value from DBORASGPR group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
