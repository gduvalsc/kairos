class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXADBIODV$$1",
            "collections": [
                "EXATOPDBIOV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, dbname label, diskv value from EXATOPDBIOV) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)