class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAFILCHOICE",
            "collection": "DBORAFIL",
            "request": "select distinct file label from DBORAFIL order by label"
        }
        super(UserObject, s).__init__(**object)
