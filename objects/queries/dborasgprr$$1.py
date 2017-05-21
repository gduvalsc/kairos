class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGPRR$$1",
            "collections": [
                "DBORASGPRR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject label, reads value from DBORASGPRR) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)