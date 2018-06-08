class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSDSKREADBYTES$$2",
            "collections": [
                "vpsutil_disk_io_counters"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'All disks'::text as label, read_bytes as value from vpsutil_disk_io_counters) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)