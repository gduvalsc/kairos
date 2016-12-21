class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGAS",
            "collection": "DBORASGA",
            "filterable": True,
            "request": "select timestamp, pool||' '||name label, sum(size) value from DBORASGA where pool = 'shared' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
