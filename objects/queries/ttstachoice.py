class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "TTSTACHOICE",
            "collection": "TTSTATS",
            "request": "select distinct statistic label from TTSTATS order by label"
        }
        super(UserObject, s).__init__(**object)
