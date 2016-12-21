class UserObject(dict):
    def __init__(s):
        if "DBORAASHWEVSQL" not in kairos: kairos['DBORAASHWEVSQL']=''
        object = {
            "type": "query",
            "id": "DBORAASHWEVSQL",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, sql_id label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_state = 'WAITING'  and sql_id != '' and event = '" + kairos["DBORAASHWEVSQL"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
