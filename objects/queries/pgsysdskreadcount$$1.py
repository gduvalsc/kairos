class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSDSKREADCOUNT$$1",
            "collections": [
                "vpsutil_disk_io_counters"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, disk as label, read_count as value from vpsutil_disk_io_counters) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)