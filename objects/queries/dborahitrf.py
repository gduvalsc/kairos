class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITRF",
            "collection": "DBORABUF",
            "request": "select timestamp, 'free buffer waits' label,  sum(freewaits) value from DBORABUF where bufpool = 'R' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
