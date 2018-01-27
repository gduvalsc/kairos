class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONIOADAPTRA$$2",
            "collections": [
                "NMONIOADAPT"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'All adapters (read)'::text as label, value / 1024.0 as value from NMONIOADAPT where id like '%read%'::text) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)