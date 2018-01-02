class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONLVCPU$$3",
            "collections": [
                "NMONCPU"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Logical CPU (computation 1) %'::text as label, avg(value) as value from (select timestamp, 'xxx'::text as label, usr + sys as value from NMONCPU where id = 'ALL') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)