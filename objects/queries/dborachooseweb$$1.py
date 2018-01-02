class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSEWEB$$1",
            "collections": [
                "DBORAWEB"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'average time (ms)' as label , avg(value) as value from (select timestamp, event as label, 1000.0 * time / count as value from DBORAWEB where event='%(DBORAWEB)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)