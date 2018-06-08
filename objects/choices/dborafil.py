class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "DBORAFIL",
            "action": "dispchart",
            "chart": "DBORACHOOSEFIL",
            "query": "DBORAFILCHOICE",
        }
        super(UserObject, s).__init__(**object)
