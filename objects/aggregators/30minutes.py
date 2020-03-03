class UserObject(dict):
    def __init__(s):
        object = {
            "type": "aggregator",
            "id": "$30minutes",
            "name": "average_per_30minutes",
            "function": """
                CREATE OR REPLACE FUNCTION average_per_30minutes(x text) RETURNS text AS $$
                    m = ["00", "30"][int(int(x[10:12]) / 30)]
                    return x[0:10] + m + "00000"
                $$ language plpython3u;
            """
        }
        super(UserObject, s).__init__(**object)
