class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHPRGCHOICE",
            "collection": "ORAHAS",
            "request": "select distinct program label from ORAHAS where program != '' order by label"
        }
        super(UserObject, s).__init__(**object)
