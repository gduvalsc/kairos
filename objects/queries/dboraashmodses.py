class UserObject(dict):
    def __init__(s):
        if "DBORAASHMODSES" not in kairos: kairos['DBORAASHMODSES']=''
        object = {
            "type": "query",
            "id": "DBORAASHMODSES",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, session_id||' - '||program label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_type = 'FOREGROUND' and module = '" + kairos["DBORAASHMODSES"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
