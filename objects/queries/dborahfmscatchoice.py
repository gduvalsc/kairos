class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSCATCHOICE",
            "collection": "ORAHQS",
            "request": "select distinct substr(force_matching_signature, 1, 2) label from ORAHQS order by label"
        }
        super(UserObject, s).__init__(**object)
