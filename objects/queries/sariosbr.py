class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARIOSBR",
            "collection": "SARB",
            "filterable": False,
            "request": "select timestamp, 'bread' label, sum(bread) value from SARB group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
