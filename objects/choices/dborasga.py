class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "DBORASGA",
            "action": "dispchart",
            "chart": "DBORACHOOSESGA",
            "query": "DBORASGACHOICE",
        }
        super(UserObject, s).__init__(**object)
