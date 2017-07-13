class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHPHVAX$$10",
            "collections": [
                "ORAHQS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Fetches' label, sum(value) value from (select timestamp, 'xxx' label, value value from (select timestamp, sum(fetches_delta) * 1.0 / (case when sum(executions_delta) = 0 then 1 else sum(executions_delta) end) value from ORAHQS where plan_hash_value = '%(DBORAHPHVAX)s' group by timestamp)) group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)