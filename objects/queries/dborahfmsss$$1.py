class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSSS$$1",
            "collections": [
                "ORAHQS",
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Elapsed'::text as label, value as value from (select h.timestamp as timestamp, coalesce(elapsed_time_delta,0)::real / 1000000.0 / m.elapsed as value from ORAHQS h, DBORAMISC m where force_matching_signature='%(DBORAHFMSSS)s' and h.timestamp=m.timestamp) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)