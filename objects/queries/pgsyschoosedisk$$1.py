class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSCHOOSEDISK$$1",
            "collections": [
                "vpsutil_disk_io_counters"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, avg(value) value from (select timestamp, 'Average time per read' label, (case when read_count = 0 then 0.0 else read_time * 1.0 / read_count end) value from vpsutil_disk_io_counters where disk = '%(PGSYSDISK)s' union all select timestamp, 'Average time per write' label, (case when write_count = 0 then 0.0 else write_time * 1.0 / write_count end) value from vpsutil_disk_io_counters where disk = '%(PGSYSDISK)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)