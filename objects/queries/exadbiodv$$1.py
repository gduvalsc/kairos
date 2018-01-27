class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXADBIODV$$1",
            "collections": [
                "EXATOPDBIOV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, dbname as label, diskv as value from EXATOPDBIOV) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)