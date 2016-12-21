class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACGCALLCU",
            "collection": "DBORARACGCTS",
            "request": "select timestamp, 'Current blocks' label, sum(cublocks) value from DBORARACGCTS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
