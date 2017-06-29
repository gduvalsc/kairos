class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSCHOOSEDISK$$4",
            "collections": [
                "vpsutil_disk_io_counters"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, avg(value) value from (select timestamp, 'Average read count per second' label, read_count value from vpsutil_disk_io_counters where disk = '%(PGSYSDISK)s' union all select timestamp, 'Average write count per second' label, write_count value from vpsutil_disk_io_counters where disk = '%(PGSYSDISK)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)