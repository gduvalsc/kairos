class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKCHOICE",
            "collection": "NMONDISKREAD",
            "request": "select distinct id label from NMONDISKREAD order by label"
        }
        super(UserObject, s).__init__(**object)
