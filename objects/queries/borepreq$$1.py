null=None
true=True
false=False

class UserObject(dict):
    def __init__(self):
        object = {
            "type": "query",
            "id": "BOREPREQ$$1",
            "collections": [
                "BO"
            ],
            "userfunctions": [
                "bocoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, report||' - '||event_id||' (duration: '||duration||')'::text as label, executecount * 1.0 / bocoeff as value from BO, (select bocoeff() as bocoeff) as foo where report = '%(BOREPREQ)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, self).__init__(**object)
