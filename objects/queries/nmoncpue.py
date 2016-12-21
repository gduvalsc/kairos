class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONCPUE",
            "collection": "NMONLPAR",
            "request": "select timestamp, id label, sum(value) value from NMONLPAR where id in ('EC_User%', 'EC_Sys%', 'EC_Wait%', 'EC_Idle%') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
