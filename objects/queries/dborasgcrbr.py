class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGCRBR",
            "collection": "DBORASGCRBR",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(blocks) value from DBORASGCRBR group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
