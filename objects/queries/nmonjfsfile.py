class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONJFSFILE",
            "collection": "NMONJFSFILE",
            "filterable": True,
            "request": "select timestamp, id label, avg(value) value from NMONJFSFILE group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
