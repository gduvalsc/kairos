class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOTOPUSR$$3",
            "collections": [
                "BO"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Response time' label, avg(value) value from (select timestamp, 'xxx' label, duration / 60.0 value from BO) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)