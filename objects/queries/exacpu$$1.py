class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXACPU$$1",
            "collections": [
                "EXACPU"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, cell label, cpu value from EXACPU) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)