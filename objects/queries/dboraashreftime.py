class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHREFTIME",
            "collections": ["ORAHAS"],
            "request": "select distinct timestamp from ORAHAS"
        }
        super(UserObject, s).__init__(**object)