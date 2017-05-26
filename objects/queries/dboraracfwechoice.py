class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACFWECHOICE",
            "collections": ["DBORARACTTFE"],
            "request": "select distinct event label from DBORARACTTFE order by label"
        }
        super(UserObject, s).__init__(**object)