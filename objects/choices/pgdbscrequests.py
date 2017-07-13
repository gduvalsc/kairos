class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "PGDBSCREQUESTS",
            "action": "dispchart",
            "chart": "PGDBSCREQUESTS",
            "query": "PGDATABASECHOICE",
        }
        super(UserObject, s).__init__(**object)
