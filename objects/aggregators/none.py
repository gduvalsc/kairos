class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$none",
            "name": "no_average",
            "numparameters": 1,
            "function": s.fnone
        }
        super(UserObject, s).__init__(**object)
    def fnone(s, x):
        return x
    def __hash__(s):
        return hash("no_average")
