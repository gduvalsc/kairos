class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQE$$2",
            "collections": [
                "DBORASQE"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Captured SQLs' label, sum(value) value from (select timestamp, 'xxx' label, elapsed value from DBORASQE) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)