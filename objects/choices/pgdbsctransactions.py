class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "PGDBSCTRANSACTIONS",
            "action": "dispchart",
            "chart": "PGDBSCTRANSACTIONS",
            "query": "PGDATABASECHOICE",
        }
        super(UserObject, s).__init__(**object)
