class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSDSKWRITECOUNT$$1",
            "collections": [
                "vpsutil_disk_io_counters"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, disk label, write_count value from vpsutil_disk_io_counters) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)