class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "DBORASV",
            "action": "dispchart",
            "chart": "DBORACHOOSESV",
            "query": "DBORASVCHOICE",
        }
        super(UserObject, s).__init__(**object)
