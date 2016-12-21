class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSQL",
            "collection": "ORAHAS",
            "filterable": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, sql_id label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_type='FOREGROUND' and sql_id != '' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
