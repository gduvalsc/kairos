class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONCPULV1",
            "collection": "NMONLPAR",
            "request": "select timestamp, 'Virtual usr+sys+idle %' label, avg(value) value from (select timestamp, 'x' label, sum(value) value from NMONLPAR where id in ('VP_User%', 'VP_Sys%', 'VP_Idle%') group by timestamp, label) group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
