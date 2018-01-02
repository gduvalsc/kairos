class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONLVCPU$$2",
            "collections": [
                "NMONLPAR"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Virtual usr+sys %'::text as label, avg(value) as value from (select timestamp, 'xxx'::text as label, value as value from (select timestamp, sum(value) as value from NMONLPAR where id in ('VP_User%', 'VP_Sys%') group by timestamp) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)