class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHSQLCATCHOICE",
            "collection": "ORAHQS",
            "request": "select distinct substr(sql_id, 1, 2) label from ORAHQS order by label"
        }
        super(UserObject, s).__init__(**object)
