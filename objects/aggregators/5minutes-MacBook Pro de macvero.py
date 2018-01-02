class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$5minutes",
            "name": "average_per_5minutes",
            "numparameters": 1,
            "function": s.f5minutes
        }
        super(UserObject, s).__init__(**object)
    def f5minutes(s, x):
        m = ["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"][int(int(x[10:12]) / 5)]
        return x[0:10] + m + "00000"
    def __hash__(s):
        return hash("average_per_5minutes")
