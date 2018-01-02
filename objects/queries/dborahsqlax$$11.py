class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHSQLAX$$11",
            "collections": [
                "ORAHQS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Rows processed'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, value as value from (select timestamp, sum(rows_processed_delta::real) * 1.0 / (case when sum(executions_delta::real) = 0 then 1 else sum(executions_delta::real) end) as value from ORAHQS where sql_id = '%(DBORAHSQLAX)s' group by timestamp) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)