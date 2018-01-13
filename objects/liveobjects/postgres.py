class UserObject(dict):
    
    def __init__(s):
        object = {
            "type": "liveobject",
            "id": "POSTGRES",
            "extension": "postgres_fdw",
            "options": "host 'postgres', port '5432', dbname 'kairos'",
            "user": "postgres",
            "password": "xxxxx",
            "tables": {
                "now": {
                    "schema": "public",
                    "description": {"now": "text"}
                },
            },
        } 
        super(UserObject, s).__init__(**object)
