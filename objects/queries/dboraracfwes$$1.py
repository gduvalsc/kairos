class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACFWES$$1",
            "collections": [
                "DBORARACTTFE"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, inum as label, timewaited as value from DBORARACTTFE where inum::int != 0 and event = '%(DBORARACFWES)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)