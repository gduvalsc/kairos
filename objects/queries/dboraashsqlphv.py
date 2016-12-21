class UserObject(dict):
    def __init__(s):
        if "DBORAASHSQLPHV" not in kairos: kairos['DBORAASHSQLPHV']=''
        object = {
            "type": "query",
            "id": "DBORAASHSQLPHV",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, sql_plan_hash_value||' - '||sql_id label, sum(kairos_count)/ashcoeff() value from ORAHAS where sql_id = '" + kairos["DBORAASHSQLPHV"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
