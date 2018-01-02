class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAWEBCHOICE",
            "collections": ["DBORAWEB"],
            "request": "select distinct event as label from DBORAWEB order by label"
        }
        super(UserObject, s).__init__(**object)