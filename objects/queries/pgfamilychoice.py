class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGFAMILYCHOICE",
            "collections": ["vpsutil_processes"],
            "request": "select distinct cmdline label from vpsutil_processes order by label"
        }
        super(UserObject, s).__init__(**object)