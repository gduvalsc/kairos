class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$12hours",
            "name": "average_per_12hours",
            "numparameters": 1,
            "function": s.f12hours
        }
        super(UserObject, s).__init__(**object)
    def f12hours(s, x):
        h = ["00", "12"][int(int(x[8:10]) / 12)]
        return x[0:8] + h + "0000000"
    def __hash__(s):
        return hash("average_per_12hours")
