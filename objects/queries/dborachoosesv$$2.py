class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSESV$$2",
            "collections": [
                "DBORASVW"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Administrative wait time'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, admwaitt as value from DBORASVW where service = '%(DBORASV)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)