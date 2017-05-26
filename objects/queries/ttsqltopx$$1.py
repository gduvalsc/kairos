class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "TTSQLTOPX$$1",
            "collections": [
                "TTSQLTOPX"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, hashid label, execs value from TTSQLTOPX) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)