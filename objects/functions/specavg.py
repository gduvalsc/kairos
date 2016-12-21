class UserObject(dict):
    def __init__(s):
        s.dict = {}
        object = {
            "type": "function",
            "id": "specavg",
            "name": "specavg",
            "numparameters": 3,
            "function": s.specavg,
            "accumulator": s.dict
        }
        super(UserObject, s).__init__(**object)
    def specavg(s, x, y, z):
        return None if x == None else x / s.dict[y+z]
    def __hash__(s):
        return hash("specavg")
