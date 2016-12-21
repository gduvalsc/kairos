class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITDF",
            "collection": "DBORABUF",
            "request": "select timestamp, 'free buffer waits' label,  sum(freewaits) value from DBORABUF where bufpool = 'D' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
