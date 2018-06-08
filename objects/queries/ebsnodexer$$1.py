class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSNODEXER$$1",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [
                "ebscoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, request_id||' (duration: '||cast(time * 60.0 as text)||')'::text as label, executecount * 1.0 / ebscoeff() as value from EBS12CM where node_name = '%(EBSNODEXER)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)