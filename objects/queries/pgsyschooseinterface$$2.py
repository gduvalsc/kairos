class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSCHOOSEINTERFACE$$2",
            "collections": [
                "vpsutil_net_io_counters"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, avg(value) value from (select timestamp, 'Average received volume per second' label, bytes_recv value from vpsutil_net_io_counters where iface = '%(PGSYSINTERFACE)s' union all select timestamp, 'Average sent volume per second' label, bytes_sent value from vpsutil_net_io_counters where iface = '%(PGSYSINTERFACE)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)