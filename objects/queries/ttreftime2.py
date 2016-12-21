class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "TTREFTIME2",
            "collection": "TTSQLHS",
            "request": "select distinct timestamp from TTSQLHS"
        }
        super(UserObject, s).__init__(**object)
