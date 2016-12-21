class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHMOD",
            "collection": "ORAHAS",
            "filterable": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, module label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_type='FOREGROUND' and module != '' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
