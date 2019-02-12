class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "TTSQLTOPP$$1",
            "collections": [
                "TTSQLTOPP"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, hashid as label, prepares as value from TTSQLTOPP) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)