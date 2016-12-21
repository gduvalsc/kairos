class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPGAAT",
            "collection": "DBORAPGA",
            "request": "select timestamp, 'PGA aggregate target' label, sum(aggrtarget) value from DBORAPGA group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
