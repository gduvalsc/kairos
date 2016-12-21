class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSUMBGSESSIONS",
            "collection": "ORAHAS",
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, 'Background DB Time' label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_type = 'BACKGROUND' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
