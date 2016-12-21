class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGIW",
            "collection": "DBORASGIW",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(waits) value from DBORASGIW group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
