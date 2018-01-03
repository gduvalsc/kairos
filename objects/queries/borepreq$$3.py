class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOREPREQ$$3",
            "collections": [
                "BO"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Response time'::text as label, avg(value) as value from (select timestamp, 'xxx'::text as label, duration::real / 60.0 as value from BO where report = '%(BOREPREQ)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)