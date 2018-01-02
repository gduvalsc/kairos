class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONIOADAPTTF$$2",
            "collections": [
                "NMONIOADAPT"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'All adapters (xfer)'::text as label, sum(value) as value from (select timestamp, 'xxx'::text as label, value / 1024.0 as value from NMONIOADAPT where id like '%xfer%'::text) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)