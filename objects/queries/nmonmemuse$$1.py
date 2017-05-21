class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONMEMUSE$$1",
            "collections": [
                "NMONMEMNEW"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, id label, value value from NMONMEMNEW where id in ('Process%','System%','FScache%','Free%')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)