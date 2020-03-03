class UserObject(dict):
    def __init__(s):
        object = {
            "type": "function",
            "id": "meet",
            "name": "meet",
            "function": """
                CREATE OR REPLACE FUNCTION meet(pattern text, regexp text) RETURNS bool AS $$
                    import re
                    return True if re.match(regexp, pattern) else False
                $$ language plpython3u;
            """
        }
        super(UserObject, s).__init__(**object)
