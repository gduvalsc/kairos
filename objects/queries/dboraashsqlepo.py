class UserObject(dict):
    def __init__(s):
        if "DBORAASHSQLEPO" not in kairos: kairos['DBORAASHSQLEPO']=''
        object = {
            "type": "query",
            "id": "DBORAASHSQLEPO",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, sql_plan_operation||' - '||sql_plan_options||' - '||sql_plan_line_id label, sum(kairos_count)/ashcoeff() value from ORAHAS where sql_id = '" + kairos["DBORAASHSQLEPO"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
