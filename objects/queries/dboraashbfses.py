class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHBFSES",
            "collection": "ORAHAS",
            "filterable": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, session_id||' - '||program  label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_type = 'FOREGROUND' and blocking_session != '' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
