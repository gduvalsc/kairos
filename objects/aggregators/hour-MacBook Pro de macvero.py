class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$hour",
            "name": "average_per_hour",
            "numparameters": 1,
            "function": s.fhour
        }
        super(UserObject, s).__init__(**object)
    def fhour(s, x):
        return x[0:10] + "0000000"
    def __hash__(s):
        return hash("average_per_hour")
