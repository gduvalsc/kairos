class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGTS$$1",
            "collections": [
                "DBORASGTS"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject label, scans value from DBORASGTS) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)