class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARREFTIME",
            "collections": ["SARU"],
            "request": "select distinct timestamp from SARU"
        }
        super(UserObject, s).__init__(**object)