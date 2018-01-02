class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$none",
            "name": "no_average",
            "function": """
                CREATE OR REPLACE FUNCTION no_average(x text) RETURNS text AS $$
	                return x
                $$ language plpythonu;
            """
        }
        super(UserObject, s).__init__(**object)