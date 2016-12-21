class UserObject(dict):
    def __init__(s):
        if "DBORAASHPRGSQL" not in kairos: kairos['DBORAASHPRGSQL']=''
        object = {
            "type": "query",
            "id": "DBORAASHPRGSQL",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, sql_id label, sum(kairos_count)/ashcoeff() value from ORAHAS where sql_id != '' and program = '" + kairos["DBORAASHPRGSQL"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
