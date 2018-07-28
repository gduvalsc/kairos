class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "SNAPPERPRGSQL",
            "action": "dispchart",
            "chart": "SNAPPERPRGSQL",
            "query": "SNAPPERPRGCHOICE",
        }
        super(UserObject, s).__init__(**object)
