class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACSUM$$1",
            "collections": [
                "DBORARACTTFE"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'wait events'::text as label, timewaited::real as value from DBORARACTTFE where inum::int = 0 and event != 'DB CPU'::text) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)