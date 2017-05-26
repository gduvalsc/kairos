class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSPRGCHOICE",
            "collections": ["EBS12CM"],
            "request": "select distinct prg_name label from EBS12CM order by label"
        }
        super(UserObject, s).__init__(**object)