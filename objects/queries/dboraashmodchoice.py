class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHMODCHOICE",
            "collection": "ORAHAS",
            "request": "select distinct module label from ORAHAS where module != '' order by label"
        }
        super(UserObject, s).__init__(**object)
