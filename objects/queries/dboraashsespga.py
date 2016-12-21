class UserObject(dict):
    def __init__(s):
        if "DBORAASHSESPGA" not in kairos: kairos['DBORAASHSESPGA']=''
        object = {
            "type": "query",
            "id": "DBORAASHSESPGA",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "request": "select timestamp, 'PGA allocated' label, sum(pga_allocated) value from ORAHAS where session_id||' - '||program = '" + kairos["DBORAASHSESPGA"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
