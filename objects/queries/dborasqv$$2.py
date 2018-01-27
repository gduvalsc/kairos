class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQV$$2",
            "collections": [
                "DBORASQV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Captured SQLs' as label, versioncount as value from DBORASQV) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)