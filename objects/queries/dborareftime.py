class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAREFTIME",
            "collection": "DBORAMISC",
            "request": "select distinct timestamp from DBORAMISC"
        }
        super(UserObject, s).__init__(**object)
