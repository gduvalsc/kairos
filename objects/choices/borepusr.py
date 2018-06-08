class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "BOREPUSR",
            "action": "dispchart",
            "chart": "BOREPUSR",
            "query": "BOREPCHOICE",
        }
        super(UserObject, s).__init__(**object)
