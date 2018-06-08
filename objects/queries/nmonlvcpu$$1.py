class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONLVCPU$$1",
            "collections": [
                "NMONLPAR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, 'Virtual usr+sys+idle %'::text as label, value as value from (select timestamp, sum(value) as value from NMONLPAR where id in ('VP_User%', 'VP_Sys%', 'VP_Idle%') group by timestamp) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)