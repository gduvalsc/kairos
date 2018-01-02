class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGLR$$1",
            "collections": [
                "DBORASGLR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject as label, gets as value from DBORASGLR) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)