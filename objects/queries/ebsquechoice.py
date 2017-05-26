class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSQUECHOICE",
            "collections": ["EBS12CM"],
            "request": "select distinct queue_name label from EBS12CM order by label"
        }
        super(UserObject, s).__init__(**object)