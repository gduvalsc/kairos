class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGDBSCHELP",
            "collections": ["vkpg_stat_activity"],
            "nocache": True,
            "request": "select distinct hash as key, query as value from vkpg_stat_activity where hash = '%(PGDBSCHELP)s' limit 1"
        }
        super(UserObject, s).__init__(**object)