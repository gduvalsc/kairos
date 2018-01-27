class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARIOS$$1",
            "collections": [
                "SARB"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'lwrite' as label, lwrite as value from SARB union all select timestamp, 'lread' as label, lread as value from SARB union all select timestamp, 'pwrite' as label, pwrite as value from SARB union all select timestamp, 'pread' as label, pread as value from SARB union all select timestamp, 'bwrite' as label, bwrite as value from SARB union all select timestamp, 'bread' as label, bread as value from SARB) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)