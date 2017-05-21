class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQX$$2",
            "collections": [
                "DBORASQX"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Captured SQLs' label, sum(value) value from (select timestamp, 'xxx' label, execs value from DBORASQX) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)