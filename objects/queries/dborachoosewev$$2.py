class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSEWEV$$2",
            "collections": [
                "DBORAWEV"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'number of operations/sec' as label , sum(value) as value from (select timestamp, event as label, count as value from DBORAWEV where event='%(DBORAWEV)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)