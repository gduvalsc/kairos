class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAWEVCHOICE",
            "collections": ["DBORAWEV"],
            "request": "select distinct event label from DBORAWEV order by label"
        }
        super(UserObject, s).__init__(**object)