class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "PGSYSCOMMAND",
            "action": "dispchart",
            "chart": "PGSYSCHOOSECOMMAND",
            "query": "PGCOMMANDCHOICE",
        }
        super(UserObject, s).__init__(**object)
