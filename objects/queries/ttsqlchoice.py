class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "TTSQLCHOICE",
            "collection": "TTSQLHS",
            "request": "select distinct hashid label from TTSQLHS order by label"
        }
        super(UserObject, s).__init__(**object)
