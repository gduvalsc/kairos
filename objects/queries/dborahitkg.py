class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITKG",
            "collection": "DBORABUF",
            "request": "select timestamp, 'gets' label,  sum(gets) value from DBORABUF where bufpool = 'K' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
