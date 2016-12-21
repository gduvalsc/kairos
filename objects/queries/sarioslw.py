class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARIOSLW",
            "collection": "SARB",
            "filterable": False,
            "request": "select timestamp, 'lwrite' label, sum(lwrite) value from SARB group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
