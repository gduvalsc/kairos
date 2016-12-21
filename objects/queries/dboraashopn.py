class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHOPN",
            "collection": "ORAHAS",
            "filterable": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, sql_opname label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_type='FOREGROUND' and sql_opname != '' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
