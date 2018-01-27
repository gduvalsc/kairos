class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVNET$$2",
            "collections": [
                "DBORAWEC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'wait events'::text as label, time as value from DBORAWEC where eclass != 'DB CPU') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)