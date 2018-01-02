class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGBBW$$1",
            "collections": [
                "DBORASGBBW"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject as label, waits as value from DBORASGBBW) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)