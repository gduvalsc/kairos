class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSPSCPUF$$1",
            "collections": [
                "vpsutil_processes"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, cmdline as label, usr + sys as value from vpsutil_processes) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)