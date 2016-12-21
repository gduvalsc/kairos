class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQG",
            "collection": "DBORASQG",
            "filterable": True,
            "request": "select timestamp, sqlid label, sum(gets) value from DBORASQG group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
