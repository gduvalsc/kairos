class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSEWEB$$3",
            "collections": [
                "DBORAWEB"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'number of timeouts/sec' as label , sum(value) as value from (select timestamp, event as label, timeouts as value from DBORAWEB where event='%(DBORAWEB)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)