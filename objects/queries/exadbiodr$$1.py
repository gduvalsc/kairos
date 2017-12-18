class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXADBIODR$$1",
            "collections": [
                "EXATOPDBIOR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, dbname label, diskr value from EXATOPDBIOR) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)