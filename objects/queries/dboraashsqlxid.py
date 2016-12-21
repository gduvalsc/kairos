class UserObject(dict):
    def __init__(s):
        if "DBORAASHSQLXID" not in kairos: kairos['DBORAASHSQLXID']=''
        object = {
            "type": "query",
            "id": "DBORAASHSQLXID",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, sql_plan_hash_value||' - '||sql_exec_id label, sum(kairos_count)/ashcoeff() value from ORAHAS where sql_id = '" + kairos["DBORAASHSQLXID"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
