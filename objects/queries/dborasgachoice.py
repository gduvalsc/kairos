class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGACHOICE",
            "collections": ["DBORASGA"],
            "request": "select distinct pool||' '||name label from DBORASGA order by label"
        }
        super(UserObject, s).__init__(**object)