class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARCPU$$2",
            "collections": [
                "SARQ"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, 'Run queue' as label, runqsz as value from SARQ union all select timestamp, 'Swap queue' as label, swpqsz as value from SARQ) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)