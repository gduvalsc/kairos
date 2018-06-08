class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHHELPP",
            "collections": ["ORAHQT", "ORAHQS"],
            "nocache": True,
            "request": "select distinct '%(DBORAHELPP)s' key, sql_text value from ORAHQT where sql_id in (select sql_id from ORAHQS where plan_hash_value = '%(DBORAHELPP)s')"
        }
        super(UserObject, s).__init__(**object)