class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQR",
            "collection": "DBORASQR",
            "filterable": True,
            "request": "select timestamp, sqlid label, sum(reads) value from DBORASQR group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
