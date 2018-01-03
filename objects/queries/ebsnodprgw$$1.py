class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSNODPRGW$$1",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [
                "ebscoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, prg_name as label, waitcount * 1.0 / ebscoeff() as value from EBS12CM where node_name = '%(EBSNODPRGW)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)