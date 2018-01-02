class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$month",
            "name": "average_per_month",
            "numparameters": 1,
            "function": s.fmonth
        }
        super(UserObject, s).__init__(**object)
    def fmonth(s, x):
        return x[0:6] + "00000000000"
    def __hash__(s):
        return hash("average_per_month")
