class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHSQLSCHOICE",
            "collections": ["ORAHQS"],
            "request": "select distinct sql_id as label from ORAHQS order by label"
        }
        super(UserObject, s).__init__(**object)