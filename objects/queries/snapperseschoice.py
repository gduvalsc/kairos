class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SNAPPERSESCHOICE",
            "collections": ["SNAPPER"],
            "request": "select distinct sid||' - '||program as label from SNAPPER order by label"
        }
        super(UserObject, s).__init__(**object)