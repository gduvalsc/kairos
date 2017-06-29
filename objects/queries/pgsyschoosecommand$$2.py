class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSCHOOSECOMMAND$$2",
            "collections": [
                "vpsutil_processes"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'Resident size' label, rss value from vpsutil_processes where pname = '%(PGSYSCOMMAND)s' union all select timestamp, 'Virtual size' label, vms value from vpsutil_processes where pname = '%(PGSYSCOMMAND)s' union all select timestamp, 'Text size' label, texts value from vpsutil_processes where pname = '%(PGSYSCOMMAND)s' union all select timestamp, 'Shared size' label, shared value from vpsutil_processes where pname = '%(PGSYSCOMMAND)s' union all select timestamp, 'Data size' label, datas value from vpsutil_processes where pname = '%(PGSYSCOMMAND)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)