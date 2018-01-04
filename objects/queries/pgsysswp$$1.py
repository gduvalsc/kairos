class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSSWP$$1",
            "collections": [
                "vpsutil_swap_memory"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Total size'::text as label, total as value from vpsutil_swap_memory union all select timestamp, 'Used size'::text as label, used as value from vpsutil_swap_memory) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)