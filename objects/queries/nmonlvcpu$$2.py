class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONLVCPU$$2",
            "collections": [
                "NMONLPAR"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Virtual usr+sys %' label, avg(value) value from (select timestamp, 'xxx' label, value value from (select timestamp, sum(value) value from NMONLPAR where id in ('VP_User%', 'VP_Sys%') group by timestamp)) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)