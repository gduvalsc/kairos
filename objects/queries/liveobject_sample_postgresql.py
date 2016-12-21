class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "LIVEOBJECT_SAMPLE_POSTGRESQL",
            "collection": "PG_STAT_ACTIVITY",
            "request": "select * from pg_stat_activity"
        }
        super(UserObject, s).__init__(**object)
