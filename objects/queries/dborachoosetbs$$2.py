class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSETBS$$2",
            "collections": [
                "DBORATBS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'number of reads per sec'::text as label , sum(value) as value from (select timestamp, 'xxx'::text as label, reads as value from DBORATBS where tablespace='%(DBORATBS)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)