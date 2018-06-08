class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSNETSENTPACKETS$$2",
            "collections": [
                "vpsutil_net_io_counters"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'All interfaces'::text as label, packets_sent as value from vpsutil_net_io_counters) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)