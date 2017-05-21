class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGCRBR$$1",
            "collections": [
                "DBORASGCRBR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject label, blocks value from DBORASGCRBR) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)