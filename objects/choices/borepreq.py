class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "BOREPREQ",
            "action": "dispchart",
            "chart": "BOREPREQ",
            "query": "BOREPCHOICE",
        }
        super(UserObject, s).__init__(**object)
