class UserObject(dict):
    def __init__(s):
        object = {
            "type": "function",
            "id": "pgdbscoeff",
            "name": "pgdbscoeff",
            "numparameters": 1,
            "function": s.pgdbscoeff
        }
        super(UserObject, s).__init__(**object)
    def pgdbscoeff(s, x):
        r = 1.0
        if 'aggregatormethod' in kairos['node']['datasource']:
            if kairos['node']['datasource']['aggregatormethod'] == '$minute': r = 60.0 / x
            if kairos['node']['datasource']['aggregatormethod'] == '$5minutes': r = 300.0 / x
            if kairos['node']['datasource']['aggregatormethod'] == '$10minutes': r = 600.0 / x
            if kairos['node']['datasource']['aggregatormethod'] == '$15minutes': r = 900.0 / x
            if kairos['node']['datasource']['aggregatormethod'] == '$20minutes': r = 1200.0 / x
            if kairos['node']['datasource']['aggregatormethod'] == '$30minutes': r = 1800.0 / x
            if kairos['node']['datasource']['aggregatormethod'] == '$hour': r = 3600.0 / x
            if kairos['node']['datasource']['aggregatormethod'] == '$2hours': r = 7200.0 / x
            if kairos['node']['datasource']['aggregatormethod'] == '$3hours': r = 10800.0 / x
            if kairos['node']['datasource']['aggregatormethod'] == '$4hours': r = 14400.0 / x
            if kairos['node']['datasource']['aggregatormethod'] == '$6hours': r = 21600.0 / x
            if kairos['node']['datasource']['aggregatormethod'] == '$12hours': r = 43200.0 / x
            if kairos['node']['datasource']['aggregatormethod'] == '$day': r = 86400.0 / x
        return r
    def __hash__(s):
        return hash("pgdbscoeff")
