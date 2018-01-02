class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$15minutes",
            "name": "average_per_15minutes",
            "numparameters": 1,
            "function": s.f15minutes
        }
        super(UserObject, s).__init__(**object)
    def f15minutes(s, x):
        m = ["00", "15", "30", "45"][int(int(x[10:12]) / 15)]
        return x[0:10] + m + "00000"
    def __hash__(s):
        return hash("average_per_15minutes")
