class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOUSRCHOICE",
            "collections": ["BO"],
            "request": "select distinct user_name as label from BO order by label"
        }
        super(UserObject, s).__init__(**object)