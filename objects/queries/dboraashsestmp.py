class UserObject(dict):
    def __init__(s):
        if "DBORAASHSESTMP" not in kairos: kairos['DBORAASHSESTMP']=''
        object = {
            "type": "query",
            "id": "DBORAASHSESTMP",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "request": "select timestamp, 'Temp space allocated' label, sum(temp_space_allocated) value from ORAHAS where session_id||' - '||program = '" + kairos["DBORAASHSESTMP"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
