class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSAX$$8",
            "collections": [
                "ORAHQS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Reads'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, value as value from (select timestamp, sum(disk_reads_delta::real) * 1.0 / (case when sum(executions_delta::real) = 0 then 1 else sum(executions_delta::real) end) as value from ORAHQS where force_matching_signature = '%(DBORAHFMSAX)s' group by timestamp) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)