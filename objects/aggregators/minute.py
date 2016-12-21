class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$minute",
            "name": "average_per_minute",
            "numparameters": 1,
            "function": s.fminute
        }
        super(UserObject, s).__init__(**object)
    def fminute(s, x):
        return x[0:12] + "00000"
    def __hash__(s):
        return hash("average_per_minute")
