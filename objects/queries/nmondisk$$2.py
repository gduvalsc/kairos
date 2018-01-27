class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISK$$2",
            "collections": [
                "NMONDISKWRITE"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Write MB/s'::text as label, value / 1024.0 as value from NMONDISKWRITE where id = '%(NMONDISK)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)