class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHPHVCATCHOICE",
            "collection": "ORAHQS",
            "request": "select distinct substr(plan_hash_value, 1, 2) label from ORAHQS order by label"
        }
        super(UserObject, s).__init__(**object)
