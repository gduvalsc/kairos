class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGRLW",
            "collection": "DBORASGRLW",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(waits) value from DBORASGRLW group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
