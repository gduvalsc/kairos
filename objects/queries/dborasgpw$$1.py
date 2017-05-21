class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGPW$$1",
            "collections": [
                "DBORASGPW"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject label, writes value from DBORASGPW) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)