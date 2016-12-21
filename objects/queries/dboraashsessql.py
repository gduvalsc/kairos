class UserObject(dict):
    def __init__(s):
        if "DBORAASHSESSQL" not in kairos: kairos['DBORAASHSESSQL']=''
        object = {
            "type": "query",
            "id": "DBORAASHSESSQL",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, sql_id label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_id||' - '||program = '" + kairos["DBORAASHSESSQL"] + "'  and sql_id != '' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
