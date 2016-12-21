class UserObject(dict):
    def __init__(s):
        if "DBORAASHSESOPN" not in kairos: kairos['DBORAASHSESOPN']=''
        object = {
            "type": "query",
            "id": "DBORAASHSESOPN",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, sql_opname label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_id||' - '||program = '" + kairos["DBORAASHSESOPN"] + "'  and sql_opname != '' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
