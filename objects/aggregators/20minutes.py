class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$20minutes",
            "name": "average_per_20minutes",
            "numparameters": 1,
            "function": s.f20minutes
        }
        super(UserObject, s).__init__(**object)
    def f20minutes(s, x):
        m = ["00", "20", "40"][int(int(x[10:12]) / 20)]
        return x[0:10] + m + "00000"
    def __hash__(s):
        return hash("average_per_20minutes")
