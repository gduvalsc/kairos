class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQRC",
            "collection": "DBORASQR",
            "request": "select timestamp, 'Captured SQLs' label, sum(reads) value from DBORASQR group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
