class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGDPW$$1",
            "collections": [
                "DBORASGDPW"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject as label, writes as value from DBORASGDPW) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)