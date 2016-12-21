class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSNODCHOICE",
            "collection": "EBS12CM",
            "request": "select distinct node_name label from EBS12CM order by label"
        }
        super(UserObject, s).__init__(**object)
