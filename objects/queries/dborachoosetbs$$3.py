class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSETBS$$3",
            "collections": [
                "DBORATBS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'database blocks per read' label, sum(value) value from (select timestamp, 'xxx' label, blocksperread value from DBORATBS where tablespace='%(DBORATBS)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)