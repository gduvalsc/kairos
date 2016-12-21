class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "TTSQLTOPX",
            "collection": "TTSQLTOPX",
            "filterable": True,
            "request": "select timestamp, hashid label, sum(execs) value from TTSQLTOPX group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
