class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORABUFPOOLCHOICE",
            "collections": ["DBORABPA"],
            "request": "select distinct bufpool as label from DBORABPA order by label"
        }
        super(UserObject, s).__init__(**object)