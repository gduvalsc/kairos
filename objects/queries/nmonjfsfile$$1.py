class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONJFSFILE$$1",
            "collections": [
                "NMONJFSFILE"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, id label, value value from NMONJFSFILE) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)