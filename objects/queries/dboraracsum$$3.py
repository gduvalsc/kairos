class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACSUM$$3",
            "collections": [
                "DBORARACTM"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'DB time'::text as label, dbtime as value from DBORARACTM) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)