class UserObject(dict):
    def __init__(s):
        if "DBORAASHPRGWEV" not in kairos: kairos['DBORAASHPRGWEV']=''
        object = {
            "type": "query",
            "id": "DBORAASHPRGWEV",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, case when event = '' then 'on cpu' when event != '' then event end label, sum(kairos_count)/ashcoeff() value from ORAHAS where program = '" + kairos["DBORAASHPRGWEV"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
