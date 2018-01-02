class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSCHOICE",
            "collections": ["ORAHQS"],
            "request": "select distinct force_matching_signature as label from ORAHQS order by label"
        }
        super(UserObject, s).__init__(**object)