class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITKB",
            "collection": "DBORABUF",
            "request": "select timestamp, 'buffer busy waits' label,  sum(busywaits) value from DBORABUF where bufpool = 'K' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
