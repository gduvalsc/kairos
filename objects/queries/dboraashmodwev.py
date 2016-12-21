class UserObject(dict):
    def __init__(s):
        if "DBORAASHMODWEV" not in kairos: kairos['DBORAASHMODWEV']=''
        object = {
            "type": "query",
            "id": "DBORAASHMODWEV",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, case when event = '' then 'on cpu' when event != '' then event end label, sum(kairos_count)/ashcoeff() value from ORAHAS where module = '" + kairos["DBORAASHMODWEV"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
