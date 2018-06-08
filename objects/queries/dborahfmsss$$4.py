class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSSS$$4",
            "collections": [
                "ORAHQS",
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Executions'::text as label, value as value from (select h.timestamp as timestamp, coalesce(executions_delta,0)::real * 1.0 / m.elapsed as value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSSS)s' and h.timestamp=m.timestamp) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)