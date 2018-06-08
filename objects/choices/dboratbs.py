class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "DBORATBS",
            "action": "dispchart",
            "chart": "DBORACHOOSETBS",
            "query": "DBORATBSCHOICE",
        }
        super(UserObject, s).__init__(**object)
