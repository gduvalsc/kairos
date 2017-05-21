class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQP$$2",
            "collections": [
                "DBORASQP"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Captured SQLs' label, sum(value) value from (select timestamp, 'xxx' label, parses value from DBORASQP) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)