class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSF$$1",
            "collections": [
                "ORAHQS",
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, force_matching_signature as label, value as value from (select h.timestamp as timestamp, force_matching_signature, coalesce(fetches_delta,0)::real * 1.0 / m.elapsed as value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)