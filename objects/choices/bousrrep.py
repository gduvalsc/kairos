class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "BOUSRREP",
            "action": "dispchart",
            "chart": "BOUSRREP",
            "query": "BOUSRCHOICE",
        }
        super(UserObject, s).__init__(**object)
