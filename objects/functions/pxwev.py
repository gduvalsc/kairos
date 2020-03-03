class UserObject(dict):
    def __init__(s):
        object = {
            "type": "function",
            "id": "pxwev",
            "name": "pxwev",
            "function": """
                CREATE OR REPLACE FUNCTION pxwev(x text) RETURNS bool AS $$
                    return True if x[0:2] in 'PX' else False
                $$ language plpython3u;
            """
        }
        super(UserObject, s).__init__(**object)
