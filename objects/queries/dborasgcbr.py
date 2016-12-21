class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGCBR",
            "collection": "DBORASGCBR",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(blocks) value from DBORASGCBR group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
