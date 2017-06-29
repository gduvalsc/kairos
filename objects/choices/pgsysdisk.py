class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "PGSYSDISK",
            "action": "dispchart",
            "chart": "PGSYSCHOOSEDISK",
            "query": "PGDISKCHOICE",
        }
        super(UserObject, s).__init__(**object)
