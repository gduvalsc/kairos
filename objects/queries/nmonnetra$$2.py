class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONNETRA$$2",
            "collections": [
                "NMONNET"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'All adapters (read)'::text as label, value / 1024.0 as value from NMONNET where id like '%read%'::text) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)