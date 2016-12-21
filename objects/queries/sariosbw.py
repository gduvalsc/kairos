class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARIOSBW",
            "collection": "SARB",
            "filterable": False,
            "request": "select timestamp, 'bwrite' label, sum(bwrite) value from SARB group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
