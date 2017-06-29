class UserObject(dict):
    def __init__(s):
        object = {
            "type": "function",
            "id": "pgdbscoeff",
            "name": "pgdbscoeff",
            "numparameters": 0,
            "function": s.pgdbscoeff
        }
        super(UserObject, s).__init__(**object)
    def pgdbscoeff(s):
        r = 1.0
        if 'aggregatormethod' in kairos['node']['datasource']:
            if kairos['node']['datasource']['aggregatormethod'] == '$minute': r = 6.0
            if kairos['node']['datasource']['aggregatormethod'] == '$5minutes': r = 30.0
            if kairos['node']['datasource']['aggregatormethod'] == '$10minutes': r = 60.0
            if kairos['node']['datasource']['aggregatormethod'] == '$15minutes': r = 90.0
            if kairos['node']['datasource']['aggregatormethod'] == '$20minutes': r = 120.0
            if kairos['node']['datasource']['aggregatormethod'] == '$30minutes': r = 180.0
            if kairos['node']['datasource']['aggregatormethod'] == '$hour': r = 360.0
            if kairos['node']['datasource']['aggregatormethod'] == '$2hours': r = 720.0
            if kairos['node']['datasource']['aggregatormethod'] == '$3hours': r = 1080.0
            if kairos['node']['datasource']['aggregatormethod'] == '$4hours': r = 1440.0
            if kairos['node']['datasource']['aggregatormethod'] == '$6hours': r = 2160.0
            if kairos['node']['datasource']['aggregatormethod'] == '$12hours': r = 4320.0
            if kairos['node']['datasource']['aggregatormethod'] == '$day': r = 8640.0
        return r
    def __hash__(s):
        return hash("pgdbscoeff")
