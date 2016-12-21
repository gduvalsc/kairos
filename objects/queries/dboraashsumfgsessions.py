class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSUMFGSESSIONS",
            "collection": "ORAHAS",
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, 'Foreground DB Time' label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_type = 'FOREGROUND' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
