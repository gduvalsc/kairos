class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSSWP$$1",
            "collections": [
                "vpsutil_swap_memory"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'Total size' label, total value from vpsutil_swap_memory union all select timestamp, 'Used size' label, used value from vpsutil_swap_memory) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)