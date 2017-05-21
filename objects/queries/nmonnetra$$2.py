class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONNETRA$$2",
            "collections": [
                "NMONNET"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'All adapters (read)' label, sum(value) value from (select timestamp, 'xxx' label, value / 1024.0 value from NMONNET where id like '%read%') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)