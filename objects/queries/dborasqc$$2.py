class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQC$$2",
            "collections": [
                "DBORASQC"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Captured SQLs' label, sum(value) value from (select timestamp, 'xxx' label, cpu value from DBORASQC) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)