class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHHELP",
            "collections": ["ORAHQT"],
            "nocache": True,
            "request": "select distinct sql_id key, sql_text value from ORAHQT where sql_id = '%(DBORAHELP)s'"
        }
        super(UserObject, s).__init__(**object)