class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSUMBGSESSIONSWAITING",
            "collection": "ORAHAS",
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, 'waiting' label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_type = 'BACKGROUND' and session_state = 'WAITING' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
