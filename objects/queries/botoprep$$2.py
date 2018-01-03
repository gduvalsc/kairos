class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOTOPREP$$2",
            "collections": [
                "BO"
            ],
            "userfunctions": [
                "bocoeff"
            ],
            "request": "select timestamp, 'All reports'::text as label, sum(value) as value from (select timestamp, 'xxx'::text as label, executecount * 1.0 / bocoeff() as value from BO) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)