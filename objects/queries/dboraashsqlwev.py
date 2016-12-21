class UserObject(dict):
    def __init__(s):
        if "DBORAASHSQLWEV" not in kairos: kairos['DBORAASHSQLWEV']=''
        object = {
            "type": "query",
            "id": "DBORAASHSQLWEV",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, case when event = '' then 'on cpu' when event != '' then event end label, sum(kairos_count)/ashcoeff() value from ORAHAS where sql_id = '" + kairos["DBORAASHSQLWEV"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
