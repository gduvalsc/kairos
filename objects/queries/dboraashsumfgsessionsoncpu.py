class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSUMFGSESSIONSONCPU",
            "collection": "ORAHAS",
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, 'on cpu' label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_type = 'FOREGROUND' and session_state = 'ON CPU' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
