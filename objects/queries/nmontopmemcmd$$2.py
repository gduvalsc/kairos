class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONTOPMEMCMD$$2",
            "collections": [
                "NMONTOP"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'All captured commands'::text as label, sum(value) as value from (select timestamp, 'xxx'::text as label, value+0.0 as value from NMONTOP where id = 'ResData'::text) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)