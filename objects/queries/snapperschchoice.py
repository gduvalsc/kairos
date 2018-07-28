class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SNAPPERSCHCHOICE",
            "collections": ["SNAPPER"],
            "request": "select distinct username as label from SNAPPER where username != '' order by label"
        }
        super(UserObject, s).__init__(**object)