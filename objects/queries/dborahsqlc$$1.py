class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHSQLC$$1",
            "collections": [
                "ORAHQS",
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, sql_id as label, value as value from (select h.timestamp as timestamp, sql_id, coalesce(cpu_time_delta,0)::real / 1000000.0 / m.elapsed as value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)