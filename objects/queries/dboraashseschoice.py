class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSESCHOICE",
            "collection": "ORAHAS",
            "request": "select distinct session_id||' - '||program label from ORAHAS order by label"
        }
        super(UserObject, s).__init__(**object)
