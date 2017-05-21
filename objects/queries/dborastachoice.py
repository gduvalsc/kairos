class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASTACHOICE",
            "collections": ["DBORASTA"],
            "request": "select distinct statistic label from DBORASTA order by label"
        }
        super(UserObject, s).__init__(**object)