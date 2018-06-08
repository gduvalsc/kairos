class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHPHVTX$$5",
            "collections": [
                "ORAHQS"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Cpu'::text as label, value as value from (select timestamp, sum(cpu_time_delta::real) / 1000000.0 / (case when sum(executions_delta::real) = 0 then 1 else sum(executions_delta::real) end) as value from ORAHQS where plan_hash_value = '%(DBORAHPHVTX)s' group by timestamp) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)