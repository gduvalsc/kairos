class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "PGSYSINTERFACE",
            "action": "dispchart",
            "chart": "PGSYSCHOOSEINTERFACE",
            "query": "PGINTERFACECHOICE",
        }
        super(UserObject, s).__init__(**object)
