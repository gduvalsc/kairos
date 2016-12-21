class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPGAWMAA",
            "collection": "DBORAPGA",
            "request": "select timestamp, 'Workarea (Manual + Auto) allocated' label, sum(memused) value from DBORAPGA group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
