class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSCPU$$1",
            "collections": [
                "vpsutil_cpu_times"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'USER_TIME' label, usr value from vpsutil_cpu_times union all select timestamp, 'SYS_TIME' label, sys value from vpsutil_cpu_times union all select timestamp, 'IOWAIT_TIME' label, iowait value from vpsutil_cpu_times) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)