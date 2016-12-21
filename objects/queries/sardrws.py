class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARDRWS",
            "collection": "SARD",
            "filterable": True,
            "request": "select timestamp, device label, sum(rws) value from SARD group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
