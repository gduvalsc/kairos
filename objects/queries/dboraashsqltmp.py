class UserObject(dict):
    def __init__(s):
        if "DBORAASHSQLTMP" not in kairos: kairos['DBORAASHSQLTMP']=''
        object = {
            "type": "query",
            "id": "DBORAASHSQLTMP",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "request": "select timestamp, 'Temp space allocated' label, sum(temp_space_allocated) value from ORAHAS where sql_id = '" + kairos["DBORAASHSQLTMP"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
