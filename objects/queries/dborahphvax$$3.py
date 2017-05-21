class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHPHVAX$$3",
            "collections": [
                "ORAHQS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'User I/O' label, sum(value) value from (select timestamp, 'xxx' label, iowait_delta / 1000000.0 / (case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where plan_hash_value='%(DBORAHPHVAX)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)