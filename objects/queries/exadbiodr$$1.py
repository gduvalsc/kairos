class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EXADBIODR$$1",
            "collections": [
                "EXATOPDBIOR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, dbname as label, diskr as value from EXATOPDBIOR) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)