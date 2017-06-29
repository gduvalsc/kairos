class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSCHOOSEINTERFACE$$1",
            "collections": [
                "vpsutil_net_io_counters"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, avg(value) value from (select timestamp, 'Average volume per received packet' label, (case when packets_recv = 0 then 0.0 else bytes_recv / packets_recv end) value from vpsutil_net_io_counters where iface = '%(PGSYSINTERFACE)s' union all select timestamp, 'Average volume per sent packet' label, (case when packets_sent = 0 then 0.0 else bytes_sent / packets_sent end) value from vpsutil_net_io_counters where iface = '%(PGSYSINTERFACE)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)