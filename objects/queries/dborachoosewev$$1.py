class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSEWEV$$1",
            "collections": [
                "DBORAWEV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, 'average time (ms)'::text as label, 1000.0 * time / count as value from DBORAWEV where event='%(DBORAWEV)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)