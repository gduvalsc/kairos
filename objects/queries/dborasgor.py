class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGOR",
            "collection": "DBORASGOR",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(reads) value from DBORASGOR group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
