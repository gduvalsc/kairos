class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITDW",
            "collection": "DBORABUF",
            "request": "select timestamp, 'write complete waits' label,  sum(writecompletewaits) value from DBORABUF where bufpool = 'D' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
