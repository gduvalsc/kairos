class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOTP",
            "collection": "DBORAWEB",
            "request": "select timestamp, event label, sum(1000.0 * time / count) value from DBORAWEB where event = 'log file parallel write' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
