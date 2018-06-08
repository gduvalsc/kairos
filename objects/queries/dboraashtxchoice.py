class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHTXCHOICE",
            "collections": ["ORAHAS"],
            "request": "select distinct xid as label from ORAHAS order by label"
        }
        super(UserObject, s).__init__(**object)