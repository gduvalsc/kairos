class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHPHVSS$$6",
            "collections": [
                "ORAHQS",
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'Rows processed'::text as label, value as value from (select h.timestamp as timestamp, coalesce(rows_processed_delta,0)::real * 1.0 / m.elapsed as value from ORAHQS h, DBORAMISC m where plan_hash_value='%(DBORAHPHVSS)s' and h.timestamp=m.timestamp) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)