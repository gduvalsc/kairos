class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGDBSREFTIME",
            "collections": ["vkpg_stat_activity"],
            "request": "select distinct timestamp from vkpg_stat_activity"
        }
        super(UserObject, s).__init__(**object)
