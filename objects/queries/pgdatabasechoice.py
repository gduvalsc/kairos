class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGDATABASECHOICE",
            "collections": ["vkpg_stat_activity"],
            "request": "select distinct datname as label from vkpg_stat_activity order by label"
        }
        super(UserObject, s).__init__(**object)