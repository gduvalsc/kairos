class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSETBS$$1",
            "collections": [
                "DBORATBS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'average time (ms)' label, avg(value) value from (select timestamp, 'xxx' label, readtime value from DBORATBS where tablespace='%(DBORATBS)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)