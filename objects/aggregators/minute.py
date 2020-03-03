class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$minute",
            "name": "average_per_minute",
            "function": """
                CREATE OR REPLACE FUNCTION average_per_minute(x text) RETURNS text AS $$
	                return x[0:12] + "00000"
                $$ language plpython3u;
            """
        }
        super(UserObject, s).__init__(**object)
