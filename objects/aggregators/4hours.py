class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$4hours",
            "name": "average_per_4hours",
            "numparameters": 1,
            "function": s.f4hours
        }
        super(UserObject, s).__init__(**object)
    def f4hours(s, x):
        h = ["00", "04", "08", "12", "16", "20"][int(int(x[8:10]) / 4)]
        return x[0:8] + h + "0000000"
    def __hash__(s):
        return hash("average_per_4hours")
