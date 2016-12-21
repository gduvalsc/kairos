class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$10minutes",
            "name": "average_per_10minutes",
            "numparameters": 1,
            "function": s.f10minutes
        }
        super(UserObject, s).__init__(**object)
    def f10minutes(s, x):
        return x[0:11] + "000000"
    def __hash__(s):
        return hash("average_per_10minutes")
