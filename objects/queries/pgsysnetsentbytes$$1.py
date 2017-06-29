class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSNETSENTBYTES$$1",
            "collections": [
                "vpsutil_net_io_counters"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, iface label, bytes_sent value from vpsutil_net_io_counters) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)