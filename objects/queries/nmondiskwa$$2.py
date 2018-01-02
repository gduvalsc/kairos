class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKWA$$2",
            "collections": [
                "NMONDISKWRITE"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Write MB/s'::text as label, sum(value) as value from (select timestamp, 'xxx'::text as label, value / 1024.0 as value from NMONDISKWRITE) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)