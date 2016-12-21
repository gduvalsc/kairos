class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGTS",
            "collection": "DBORASGTS",
            "filterable": True,
            "request": "select timestamp, owner||' '||objtype||' '||object||' '||subobject label, sum(scans) value from DBORASGTS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
