class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOT$$3",
            "collections": [
                "DBORAWEB"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, event label, 1000.0 * time / count value from DBORAWEB where event='log file parallel write') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)