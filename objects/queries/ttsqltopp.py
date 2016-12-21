class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "TTSQLTOPP",
            "collection": "TTSQLTOPP",
            "filterable": True,
            "request": "select timestamp, hashid label, sum(prepares) value from TTSQLTOPP group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
