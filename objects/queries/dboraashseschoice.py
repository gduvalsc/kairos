class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSESCHOICE",
            "collections": ["ORAHAS"],
            "request": "select distinct session_id||' - '||program label from ORAHAS order by label"
        }
        super(UserObject, s).__init__(**object)