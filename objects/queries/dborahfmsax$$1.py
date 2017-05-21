class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSAX$$1",
            "collections": [
                "ORAHQS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Application' label, sum(value) value from (select timestamp, 'xxx' label, apwait_delta / 1000000.0 / (case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where force_matching_signature='%(DBORAHFMSAX)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)