class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACFWEA$$1",
            "collections": [
                "DBORARACTTFE"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, inum label, 1000.0 * timewaited / waits value from DBORARACTTFE where inum != 0 and event = '%(DBORARACFWES)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)