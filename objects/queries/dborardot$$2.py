class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOT$$2",
            "collections": [
                "DBORAWEV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, event as label, 1000.0 * time / count as value from DBORAWEV where event='log file sync') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)