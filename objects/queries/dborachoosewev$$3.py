class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSEWEV$$3",
            "collections": [
                "DBORAWEV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'number of timeouts/sec' as label, timeouts as value from DBORAWEV where event='%(DBORAWEV)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)