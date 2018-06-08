class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSPSMEMRSSF$$1",
            "collections": [
                "vpsutil_processes"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, cmdline as label, rss::real as value from vpsutil_processes) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)