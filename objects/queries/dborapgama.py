class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPGAMA",
            "collection": "DBORAPGA",
            "request": "select timestamp, 'Memory allocated' label, sum(memalloc) value from DBORAPGA group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
