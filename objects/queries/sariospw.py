class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARIOSPW",
            "collection": "SARB",
            "filterable": False,
            "request": "select timestamp, 'pwrite' label, sum(pwrite) value from SARB group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
