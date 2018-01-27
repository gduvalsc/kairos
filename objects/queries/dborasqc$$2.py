class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQC$$2",
            "collections": [
                "DBORASQC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Captured SQLs' as label, cpu as value from DBORASQC) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)