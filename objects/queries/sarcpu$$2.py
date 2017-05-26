class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARCPU$$2",
            "collections": [
                "SARQ"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, avg(value) value from (select timestamp, 'Run queue' label, runqsz value from SARQ union all select timestamp, 'Swap queue' label, swpqsz value from SARQ) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)