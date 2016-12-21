class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPGAMOA",
            "collection": "DBORAPGA",
            "request": "select timestamp, 'Memory other allocated' label, sum(memalloc - memused) value from DBORAPGA group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
