class UserObject(dict):
    def __init__(s):
        if "DBORAASHMODSQL" not in kairos: kairos['DBORAASHMODSQL']=''
        object = {
            "type": "query",
            "id": "DBORAASHMODSQL",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, sql_id label, sum(kairos_count)/ashcoeff() value from ORAHAS where sql_id != '' and module = '" + kairos["DBORAASHMODSQL"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
