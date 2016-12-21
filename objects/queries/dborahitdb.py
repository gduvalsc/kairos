class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITDB",
            "collection": "DBORABUF",
            "request": "select timestamp, 'buffer busy waits' label,  sum(busywaits) value from DBORABUF where bufpool = 'D' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
