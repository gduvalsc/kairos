class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACREFTIME",
            "collections": ["DBORARACMISC"],
            "request": "select distinct timestamp from DBORARACMISC"
        }
        super(UserObject, s).__init__(**object)