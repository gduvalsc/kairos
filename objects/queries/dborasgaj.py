class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGAJ",
            "collection": "DBORASGA",
            "filterable": True,
            "request": "select timestamp, pool||' '||name label, sum(size) value from DBORASGA where pool = 'java' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
