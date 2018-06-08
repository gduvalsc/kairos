class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOREPUSR$$3",
            "collections": [
                "BO"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, 'Response time'::text as label, duration::real / 60.0 as value from BO where report = '%(BOREPUSR)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)