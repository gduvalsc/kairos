class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$day",
            "name": "average_per_day",
            "numparameters": 1,
            "function": s.fday
        }
        super(UserObject, s).__init__(**object)
    def fday(s, x):
        return x[0:8] + "000000000"
    def __hash__(s):
        return hash("average_per_day")
