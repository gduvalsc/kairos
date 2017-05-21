class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSETBS$$2",
            "collections": [
                "DBORATBS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'number of reads per sec' label, sum(value) value from (select timestamp, 'xxx' label, reads value from DBORATBS where tablespace='%(DBORATBS)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)