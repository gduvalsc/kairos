class UserObject(dict):
    def __init__(s):
        if "DBORAASHSESWEV" not in kairos: kairos['DBORAASHSESWEV']=''
        object = {
            "type": "query",
            "id": "DBORAASHSESWEV",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, case when event = '' then 'on cpu' when event != '' then event end label, sum(kairos_count)/ashcoeff() value from ORAHAS where session_id||' - '||program = '" + kairos["DBORAASHSESWEV"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
