class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHHELPF",
            "collections": ["ORAHQT", "ORAHQS"],
            "nocache": True,
            "request": "select distinct '%(DBORAHELPF)s' key, sql_text value from ORAHQT where sql_id in (select sql_id from ORAHQS where force_matching_signature = '%(DBORAHELPF)s')"
        }
        super(UserObject, s).__init__(**object)