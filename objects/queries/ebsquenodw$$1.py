class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSQUENODW$$1",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [
                "ebscoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, node_name as label, waitcount * 1.0 / ebscoeff() as value from EBS12CM where queue_name = '%(EBSQUENODW)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)