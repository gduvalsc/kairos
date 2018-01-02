class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALIBR$$2",
            "collections": [
                "DBORALIB"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Reloads'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, reloads as value from DBORALIB) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)