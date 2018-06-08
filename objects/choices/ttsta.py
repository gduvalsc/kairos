class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "TTSTA",
            "action": "dispchart",
            "chart": "TTSTA",
            "query": "TTSTACHOICE",
        }
        super(UserObject, s).__init__(**object)
