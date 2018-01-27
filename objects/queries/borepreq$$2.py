class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOREPREQ$$2",
            "collections": [
                "BO"
            ],
            "userfunctions": [
                "bocoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'All requests'::text as label, executecount * 1.0 / bocoeff() as value from BO where report = '%(BOREPREQ)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)