class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALOGONS1",
            "collection": "DBORAMISC",
            "request": "select timestamp, 'sessions' label, sum(sessions) value from DBORAMISC group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
