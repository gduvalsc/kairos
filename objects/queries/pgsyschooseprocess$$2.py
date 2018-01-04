class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSCHOOSEPROCESS$$2",
            "collections": [
                "vpsutil_processes"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Resident size'::text as label, rss as value from vpsutil_processes where pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'::text union all select timestamp, 'Virtual size'::text as label, vms as value from vpsutil_processes where pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'::text union all select timestamp, 'Text size'::text as label, texts as value from vpsutil_processes where pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'::text union all select timestamp, 'Shared size'::text as label, shared as value from vpsutil_processes where pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'::text union all select timestamp, 'Data size'::text as label, datas as value from vpsutil_processes where pname||' - '||pid||' - '||create_time = '%(PGSYSPROCESS)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)