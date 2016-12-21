class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOTL",
            "collection": "DBORAWEV",
            "request": "select timestamp, event label, sum(1000.0 * time / count) value from DBORAWEV where event = 'log file sync' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
