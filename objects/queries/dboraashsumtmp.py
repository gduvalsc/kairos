class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSUMTMP",
            "collection": "ORAHAS",
            "request": "select timestamp, 'Temp space allocated' label, sum(temp_space_allocated) value from ORAHAS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
