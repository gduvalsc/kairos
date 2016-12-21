class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITKR",
            "collection": "DBORABUF",
            "request": "select timestamp, 'reads' label,  sum(reads) value from DBORABUF where bufpool = 'K' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
