class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITDG",
            "collection": "DBORABUF",
            "request": "select timestamp, 'gets' label,  sum(gets) value from DBORABUF where bufpool = 'D' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
