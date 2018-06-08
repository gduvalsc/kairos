class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGDBREFTIME",
            "collections": ["vkpg_stat_database"],
            "request": "select distinct timestamp from vkpg_stat_database"
        }
        super(UserObject, s).__init__(**object)
