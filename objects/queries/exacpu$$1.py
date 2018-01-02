class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXACPU$$1",
            "collections": [
                "EXACPU"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, cell as label, cpu as value from EXACPU) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)