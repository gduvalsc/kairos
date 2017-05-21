class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGGCBB$$1",
            "collections": [
                "DBORASGGCBB"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject label, waits value from DBORASGGCBB) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)