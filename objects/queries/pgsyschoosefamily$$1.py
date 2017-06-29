class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSCHOOSEFAMILY$$1",
            "collections": [
                "vpsutil_processes"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'USER_TIME' label, usr value from vpsutil_processes where cmdline = '%(PGSYSFAMILY)s' union all select timestamp, 'SYS_TIME' label, sys value from vpsutil_processes where cmdline = '%(PGSYSFAMILY)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)