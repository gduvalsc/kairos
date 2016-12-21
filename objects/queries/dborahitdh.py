class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITDH",
            "collection": "DBORABUF",
            "request": "select timestamp, 'hit ratio' label,  sum(100.0 * (1 - (reads / gets))) value from DBORABUF where bufpool = 'D' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
