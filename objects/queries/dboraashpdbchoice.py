class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHPDBCHOICE",
            "collections": ["ORAHAS"],
            "request": "select distinct con_name as label from ORAHAS order by label"
        }
        super(UserObject, s).__init__(**object)