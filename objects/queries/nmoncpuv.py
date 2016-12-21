class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONCPUV",
            "collection": "NMONLPAR",
            "request": "select timestamp, id label, sum(value) value from NMONLPAR where id in ('VP_User%', 'VP_Sys%', 'VP_Wait%', 'VP_Idle%') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
