class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPDBCHOICE",
            "collections": ["DBORAINFO"],
            "request": "select distinct  cname as label from DBORAINFO order by label"
        }
        super(UserObject, s).__init__(**object)