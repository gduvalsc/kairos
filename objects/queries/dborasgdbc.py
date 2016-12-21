class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGDBC",
            "collection": "DBORASGDBC",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(changes) value from DBORASGDBC group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
