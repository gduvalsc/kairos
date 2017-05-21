class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHMODCHOICE",
            "collections": ["ORAHAS"],
            "request": "select distinct module label from ORAHAS where module != '' order by label"
        }
        super(UserObject, s).__init__(**object)