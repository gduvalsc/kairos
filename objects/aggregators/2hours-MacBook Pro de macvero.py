class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$2hours",
            "name": "average_per_2hours",
            "numparameters": 1,
            "function": s.f2hours
        }
        super(UserObject, s).__init__(**object)
    def f2hours(s, x):
        h = ["00", "02", "04", "06", "08", "10", "12", "14", "16", "18", "20", "22"][int(int(x[8:10]) / 2)]
        return x[0:8] + h + "0000000"
    def __hash__(s):
        return hash("average_per_2hours")
