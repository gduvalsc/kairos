class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARIOS$$1",
            "collections": [
                "SARB"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'lwrite' label, lwrite value from SARB union all select timestamp, 'lread' label, lread value from SARB union all select timestamp, 'pwrite' label, pwrite value from SARB union all select timestamp, 'pread' label, pread value from SARB union all select timestamp, 'bwrite' label, bwrite value from SARB union all select timestamp, 'bread' label, bread value from SARB) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)