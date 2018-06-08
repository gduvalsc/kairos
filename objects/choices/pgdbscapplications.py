class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "PGDBSCAPPLICATIONS",
            "action": "dispchart",
            "chart": "PGDBSCAPPLICATIONS",
            "query": "PGDATABASECHOICE",
        }
        super(UserObject, s).__init__(**object)
