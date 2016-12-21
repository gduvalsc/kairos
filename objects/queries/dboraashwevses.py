class UserObject(dict):
    def __init__(s):
        if "DBORAASHWEVSES" not in kairos: kairos['DBORAASHWEVSES']=''
        object = {
            "type": "query",
            "id": "DBORAASHWEVSES",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, session_id||' - '||program label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_type = 'FOREGROUND' and session_state = 'WAITING' and event = '" + kairos["DBORAASHWEVSES"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
