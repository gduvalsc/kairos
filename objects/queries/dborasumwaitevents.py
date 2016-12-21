class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUMWAITEVENTS",
            "collection": "DBORAWEC",
            "request": "select timestamp, 'wait events' label, sum(time) value from DBORAWEC where eclass != 'DB CPU' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
