class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVCHOICE",
            "collections": ["DBORASRV"],
            "request": "select distinct service label from DBORASRV order by label"
        }
        super(UserObject, s).__init__(**object)