class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACDBWAITBEI$$2",
            "collections": [
                "DBORARACTTBE"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Wait events'::text as label, timewaited as value from DBORARACTTBE where inum::int = 0 and event != 'background cpu time'::text) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)