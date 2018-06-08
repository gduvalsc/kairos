class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGTS$$1",
            "collections": [
                "DBORASGTS"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject as label, scans as value from DBORASGTS) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)