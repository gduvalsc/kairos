class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSCPU$$2",
            "collections": [
                "vpsutil_cpu_times"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'NUM_CPUS'::text as label, nbcpus as value from vpsutil_cpu_times) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)