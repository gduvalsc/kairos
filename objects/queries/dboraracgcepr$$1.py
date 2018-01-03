class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACGCEPR$$1",
            "collections": [
                "DBORARACGCEP"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, inum as label, premote as value from DBORARACGCEP) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)