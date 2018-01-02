class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQG$$2",
            "collections": [
                "DBORASQG"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Captured SQLs'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, gets as value from DBORASQG) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)