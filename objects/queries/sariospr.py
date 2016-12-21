class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARIOSPR",
            "collection": "SARB",
            "filterable": False,
            "request": "select timestamp, 'pread' label, sum(pread) value from SARB group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
