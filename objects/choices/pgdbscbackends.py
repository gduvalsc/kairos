class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "PGDBSCBACKENDS",
            "action": "dispchart",
            "chart": "PGDBSCBACKENDS",
            "query": "PGDATABASECHOICE",
        }
        super(UserObject, s).__init__(**object)
