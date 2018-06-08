class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQE$$2",
            "collections": [
                "DBORASQE"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Captured SQLs'::text as label, elapsed as value from DBORASQE) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)