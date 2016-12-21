class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "NMONDISK",
            "action": "dispchart",
            "chart": "NMONDISK",
            "query": "NMONDISKCHOICE",
        }
        super(UserObject, s).__init__(**object)
