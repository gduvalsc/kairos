class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSSX$$1",
            "collections": [
                "ORAHQS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Elapsed' label, sum(value) value from (select timestamp, 'xxx' label, value value from (select timestamp, sum(elapsed_time_delta) / 1000000.0 / (case when sum(executions_delta) = 0 then 1 else sum(executions_delta) end) value from ORAHQS where force_matching_signature = '%(DBORAHFMSSX)s' group by timestamp)) group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)