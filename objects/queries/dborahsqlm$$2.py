class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHSQLM$$2",
            "collections": [
                "ORAHQS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Captured SQLs'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, sharable_mem as value from ORAHQS) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)