class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQR$$2",
            "collections": [
                "DBORASQR"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Captured SQLs' label, sum(value) value from (select timestamp, 'xxx' label, reads value from DBORASQR) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)