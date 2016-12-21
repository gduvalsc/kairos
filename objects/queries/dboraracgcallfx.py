class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACGCALLFX",
            "collection": "DBORARACGCTS",
            "request": "select timestamp, 'From '||src label, sum(cublocks+crblocks) value from DBORARACGCTS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
