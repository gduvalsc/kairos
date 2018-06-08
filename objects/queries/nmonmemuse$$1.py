class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONMEMUSE$$1",
            "collections": [
                "NMONMEMNEW"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, id as label, value as value from NMONMEMNEW where id in ('Process%','System%','FScache%','Free%')) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)