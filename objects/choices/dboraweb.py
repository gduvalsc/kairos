class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "DBORAWEB",
            "action": "dispchart",
            "chart": "DBORACHOOSEWEB",
            "query": "DBORAWEBCHOICE",
        }
        super(UserObject, s).__init__(**object)
