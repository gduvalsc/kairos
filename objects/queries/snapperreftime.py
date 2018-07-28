class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SNAPPERREFTIME",
            "collections": ["SNAPPER"],
            "request": "select distinct timestamp from SNAPPER"
        }
        super(UserObject, s).__init__(**object)