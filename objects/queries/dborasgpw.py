class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGPW",
            "collection": "DBORASGPW",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(writes) value from DBORASGPW group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
