class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGAJ$$1",
            "collections": [
                "DBORASGA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, pool||' '||name label, size value from DBORASGA where pool = 'java') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)