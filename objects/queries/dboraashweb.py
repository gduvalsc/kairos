class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHWEB",
            "collection": "ORAHAS",
            "filterable": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, event label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_type = 'BACKGROUND' and session_state = 'WAITING' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
