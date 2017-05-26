class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "TTREFTIME",
            "collections": ["TTMISC"],
            "request": "select distinct timestamp from TTMISC"
        }
        super(UserObject, s).__init__(**object)