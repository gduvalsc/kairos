class UserObject(dict):
    def __init__(s):
        object = {
            "type": "choice",
            "id": "PGSYSFAMILY",
            "action": "dispchart",
            "chart": "PGSYSCHOOSEFAMILY",
            "query": "PGFAMILYCHOICE",
        }
        super(UserObject, s).__init__(**object)
