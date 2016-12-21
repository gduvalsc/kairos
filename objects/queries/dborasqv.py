class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQV",
            "collection": "DBORASQV",
            "filterable": True,
            "request": "select timestamp, sqlid label, sum(versioncount) value from DBORASQV group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
