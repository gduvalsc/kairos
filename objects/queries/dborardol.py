class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOL",
            "collection": "DBORAWEV",
            "request": "select timestamp, event label, sum(time) value from DBORAWEV where event = 'log file sync' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
