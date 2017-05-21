class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGDPW$$1",
            "collections": [
                "DBORASGDPW"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject label, writes value from DBORASGDPW) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)