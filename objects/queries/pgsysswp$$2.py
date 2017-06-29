class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSSWP$$2",
            "collections": [
                "vpsutil_swap_memory"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'Swap in' label, sin value from vpsutil_swap_memory union all select timestamp, 'Swap out' label, sout value from vpsutil_swap_memory) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)