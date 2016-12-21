class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$6hours",
            "name": "average_per_6hours",
            "numparameters": 1,
            "function": s.f6hours
        }
        super(UserObject, s).__init__(**object)
    def f6hours(s, x):
        h = ["00", "06", "12", "18"][int(int(x[8:10]) / 6)]
        return x[0:8] + h + "0000000"
    def __hash__(s):
        return hash("average_per_6hours")
