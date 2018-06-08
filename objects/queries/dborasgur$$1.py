class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGUR$$1",
            "collections": [
                "DBORASGUR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject as label, reads as value from DBORASGUR) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)