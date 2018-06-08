class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOREPUSR$$1",
            "collections": [
                "BO"
            ],
            "userfunctions": [
                "bocoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, user_name as label, executecount * 1.0 / bocoeff() as value from BO where report = '%(BOREPUSR)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)