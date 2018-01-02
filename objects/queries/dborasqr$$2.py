class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQR$$2",
            "collections": [
                "DBORASQR"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Captured SQLs' as label , sum(value) as value from (select timestamp, 'xxx'::text as label, reads as value from DBORASQR) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)