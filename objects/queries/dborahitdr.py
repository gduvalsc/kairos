class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITDR",
            "collection": "DBORABUF",
            "request": "select timestamp, 'reads' label,  sum(reads) value from DBORABUF where bufpool = 'D' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
