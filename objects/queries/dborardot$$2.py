class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOT$$2",
            "collections": [
                "DBORAWEV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, event label, 1000.0 * time / count value from DBORAWEV where event='log file sync') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)