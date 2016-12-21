class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACGCCUFX",
            "collection": "DBORARACGCTS",
            "request": "select timestamp, 'From '||src label, sum(cublocks) value from DBORARACGCTS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
