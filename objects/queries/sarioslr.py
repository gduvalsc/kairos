class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARIOSLR",
            "collection": "SARB",
            "filterable": False,
            "request": "select timestamp, 'lread' label, sum(lread) value from SARB group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
