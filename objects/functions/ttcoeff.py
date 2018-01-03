class UserObject(dict):
    def __init__(s):
        object = {
            "type": "function",
            "id": "ttcoeff",
            "name": "ttcoeff",
            "function": """
                CREATE OR REPLACE FUNCTION ttcoeff() RETURNS real AS $$
                    try: method = plpy.execute("select method from aggregator",1)[0]['method']
                    except: method = '$none'
                    r = 1.0
                    if method == '$15minutes': r = 1.0
                    if method == '$30minutes': r = 2.0
                    if method == '$hour': r = 4.0
                    if method == '$2hours': r = 8.0
                    if method == '$3hours': r = 12.0
                    if method == '$4hours': r = 16.0
                    if method == '$6hours': r = 24.0
                    if method == '$8hours': r = 32.0
                    if method == '$12hours': r = 48.0
                    if method == '$day': r = 96.0
                    return r
                $$ language plpythonu;
            """
        }
        super(UserObject, s).__init__(**object)
