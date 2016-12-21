class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAWEBCHOICE",
            "collection": "DBORAWEB",
            "request": "select distinct event label from DBORAWEB order by label"
        }
        super(UserObject, s).__init__(**object)
