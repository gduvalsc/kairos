class UserObject(dict):
    def __init__(s):
        object = {
            "type": "function",
            "id": "specavg",
            "name": "specavg",
            "function": """
                CREATE OR REPLACE FUNCTION specavg(x real, y text, z text, t jsonb) RETURNS real AS $$
                    import json
                    d = json.loads(t)
                    return None if x == None else x / d[y+z]
                $$ language plpythonu;
            """
        }
        super(UserObject, s).__init__(**object)
