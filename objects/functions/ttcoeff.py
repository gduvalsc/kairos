class UserObject(dict):
    def __init__(s):
        object = {
            "type": "function",
            "id": "ttcoeff",
            "name": "ttcoeff",
            "numparameters": 0,
            "function": s.ttcoeff
        }
        super(UserObject, s).__init__(**object)
    def ttcoeff(s):
        r = 1.0
        if 'aggregatormethod' in kairos['node']['datasource']:
            if kairos['node']['datasource']['aggregatormethod'] == '$hour': r = 4.0
            if kairos['node']['datasource']['aggregatormethod'] == '$day': r = 96.0
        return r
    def __hash__(s):
        return hash("ttcoeff")
