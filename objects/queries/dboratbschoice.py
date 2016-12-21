class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORATBSCHOICE",
            "collection": "DBORATBS",
            "request": "select distinct tablespace label from DBORATBS order by label"
        }
        super(UserObject, s).__init__(**object)
