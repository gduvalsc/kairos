class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKRA$$2",
            "collections": [
                "NMONDISKREAD"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Read MB/s'::text as label, value / 1024.0 as value from NMONDISKREAD) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)