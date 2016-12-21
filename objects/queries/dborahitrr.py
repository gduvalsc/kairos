class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITRR",
            "collection": "DBORABUF",
            "request": "select timestamp, 'reads' label,  sum(reads) value from DBORABUF where bufpool = 'R' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
