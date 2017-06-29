class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSDSKWRITEBYTES$$2",
            "collections": [
                "vpsutil_disk_io_counters"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'All disks' label, write_bytes value from vpsutil_disk_io_counters) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)