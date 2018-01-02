class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHPHVCHOICE",
            "collections": ["ORAHQS"],
            "request": "select distinct plan_hash_value as label from ORAHQS order by label"
        }
        super(UserObject, s).__init__(**object)