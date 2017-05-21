class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITD$$1",
            "collections": [
                "DBORABUF"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'gets' label, sum(value) value from (select timestamp, 'xxx' label, gets value from DBORABUF where bufpool='D') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)