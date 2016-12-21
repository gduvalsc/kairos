class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGLR",
            "collection": "DBORASGLR",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(gets) value from DBORASGLR group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
