class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "DBORABUFPOOL",
            "action": "dispchart",
            "chart": "DBORACHOOSEBUFPOOL",
            "query": "DBORABUFPOOLCHOICE",
        }
        super(UserObject, s).__init__(**object)
