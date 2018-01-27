class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGCBR$$1",
            "collections": [
                "DBORASGCBR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject as label, blocks as value from DBORASGCBR) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)