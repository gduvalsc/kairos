class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGBBW",
            "collection": "DBORASGBBW",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(waits) value from DBORASGBBW group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
