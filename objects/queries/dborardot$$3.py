class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOT$$3",
            "collections": [
                "DBORAWEB"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, event as label, 1000.0 * time / count as value from DBORAWEB where event='log file parallel write') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)