class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SNAPPERPRGCHOICE",
            "collections": ["SNAPPER"],
            "request": "select distinct program as label from SNAPPER where program != '' order by label"
        }
        super(UserObject, s).__init__(**object)