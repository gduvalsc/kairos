class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSETBS$$1",
            "collections": [
                "DBORATBS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'average time (ms)'::text as label , avg(value) as value from (select timestamp, 'xxx'::text as label, readtime as value from DBORATBS where tablespace='%(DBORATBS)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)