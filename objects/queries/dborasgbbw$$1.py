class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGBBW$$1",
            "collections": [
                "DBORASGBBW"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject label, waits value from DBORASGBBW) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)