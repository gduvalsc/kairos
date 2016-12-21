class UserObject(dict):
    def __init__(s):
        if "DBORAASHSQLSES" not in kairos: kairos['DBORAASHSQLSES']=''
        object = {
            "type": "query",
            "id": "DBORAASHSQLSES",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, session_id||' - '||program label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_type = 'FOREGROUND' and sql_id = '" + kairos["DBORAASHSQLSES"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
