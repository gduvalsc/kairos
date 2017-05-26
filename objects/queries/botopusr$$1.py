class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOTOPUSR$$1",
            "collections": [
                "BO"
            ],
            "userfunctions": [
                "bocoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, user_name label, executecount * 1.0 / bocoeff() value from BO) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)