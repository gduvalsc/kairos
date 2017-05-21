class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGUR$$1",
            "collections": [
                "DBORASGUR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject label, reads value from DBORASGUR) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)