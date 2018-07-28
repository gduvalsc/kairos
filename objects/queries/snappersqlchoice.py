class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SNAPPERSQLCHOICE",
            "collections": ["SNAPPER"],
            "request": "select distinct sql_id as label from SNAPPER where sql_id != '' order by label"
        }
        super(UserObject, s).__init__(**object)