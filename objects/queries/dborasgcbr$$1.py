class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGCBR$$1",
            "collections": [
                "DBORASGCBR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject label, blocks value from DBORASGCBR) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)