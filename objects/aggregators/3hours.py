class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$3hours",
            "name": "average_per_3hours",
            "numparameters": 1,
            "function": s.f3hours
        }
        super(UserObject, s).__init__(**object)
    def f3hours(s, x):
        h = ["00", "03", "06", "09", "12", "15", "18", "21"][int(int(x[8:10]) / 3)]
        return x[0:8] + h + "0000000"
    def __hash__(s):
        return hash("average_per_3hours")
