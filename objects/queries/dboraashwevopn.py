class UserObject(dict):
    def __init__(s):
        if "DBORAASHWEVOPN" not in kairos: kairos['DBORAASHWEVOPN']=''
        object = {
            "type": "query",
            "id": "DBORAASHWEVOPN",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, sql_opname label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_state = 'WAITING'  and sql_opname != '' and event = '" + kairos["DBORAASHWEVOPN"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
