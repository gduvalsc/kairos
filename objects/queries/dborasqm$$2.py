class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQM$$2",
            "collections": [
                "DBORASQM"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Captured SQLs' label, sum(value) value from (select timestamp, 'xxx' label, sharedmem value from DBORASQM) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)