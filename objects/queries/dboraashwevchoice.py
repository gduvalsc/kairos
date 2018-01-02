class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHWEVCHOICE",
            "collections": ["ORAHAS"],
            "request": "select distinct event as label from ORAHAS where session_state = 'WAITING' order by label"
        }
        super(UserObject, s).__init__(**object)