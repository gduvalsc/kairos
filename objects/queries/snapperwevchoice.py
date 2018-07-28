class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SNAPPERWEVCHOICE",
            "collections": ["SNAPPER"],
            "request": "select distinct event as label from SNAPPER where event  != 'ON CPU' order by label"
        }
        super(UserObject, s).__init__(**object)