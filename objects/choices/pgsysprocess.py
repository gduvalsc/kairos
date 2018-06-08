class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "PGSYSPROCESS",
            "action": "dispchart",
            "chart": "PGSYSCHOOSEPROCESS",
            "query": "PGPROCESSCHOICE",
        }
        super(UserObject, s).__init__(**object)
