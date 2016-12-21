class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGUR",
            "collection": "DBORASGUR",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(reads) value from DBORASGUR group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
