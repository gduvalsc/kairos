class UserObject(dict):
    def __init__(s):
        if "DBORAASHPRGSES" not in kairos: kairos['DBORAASHPRGSES']=''
        object = {
            "type": "query",
            "id": "DBORAASHPRGSES",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, session_id||' - '||program label, sum(kairos_count)/ashcoeff() value from ORAHAS where program = '" + kairos["DBORAASHPRGSES"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
