class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "TTSTACHOICE",
            "collections": ["TTSTATS"],
            "request": "select distinct statistic as label from TTSTATS order by label"
        }
        super(UserObject, s).__init__(**object)