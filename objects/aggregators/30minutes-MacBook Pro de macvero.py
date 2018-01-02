class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$30minutes",
            "name": "average_per_30minutes",
            "numparameters": 1,
            "function": s.f30minutes
        }
        super(UserObject, s).__init__(**object)
    def f30minutes(s, x):
        m = ["00", "30"][int(int(x[10:12]) / 30)]
        return x[0:10] + m + "00000"
    def __hash__(s):
        return hash("average_per_30minutes")
