class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSCPU$$2",
            "collections": [
                "vpsutil_cpu_times"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'NUM_CPUS' label, nbcpus value from vpsutil_cpu_times) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)