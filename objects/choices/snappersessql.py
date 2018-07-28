class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "SNAPPERSESSQL",
            "action": "dispchart",
            "chart": "SNAPPERSESSQL",
            "query": "SNAPPERSESCHOICE",
        }
        super(UserObject, s).__init__(**object)
