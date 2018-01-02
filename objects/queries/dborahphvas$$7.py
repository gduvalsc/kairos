class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHPHVAS$$7",
            "collections": [
                "ORAHQS",
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Gets'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, value as value from (select h.timestamp as timestamp, coalesce(buffer_gets_delta,0)::real * 1.0 / m.elapsed as value from ORAHQS h, DBORAMISC m where plan_hash_value='%(DBORAHPHVAS)s' and h.timestamp=m.timestamp) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)