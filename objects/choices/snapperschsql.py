class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "SNAPPERSCHSQL",
            "action": "dispchart",
            "chart": "SNAPPERSCHSQL",
            "query": "SNAPPERSCHCHOICE",
        }
        super(UserObject, s).__init__(**object)
