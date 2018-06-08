class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAWEHCHOICE",
            "collections": ["DBORAWEH"],
            "request": "select distinct event as label from DBORAWEH order by label"
        }
        super(UserObject, s).__init__(**object)