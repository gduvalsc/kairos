class UserObject(dict):
    def __init__(s):
        if "DBORAASHSQLPGA" not in kairos: kairos['DBORAASHSQLPGA']=''
        object = {
            "type": "query",
            "id": "DBORAASHSQLPGA",
            "collection": "ORAHAS",
            "filterable": True,
            "nocache": True,
            "request": "select timestamp, 'PGA allocated' label, sum(pga_allocated) value from ORAHAS where sql_id = '" + kairos["DBORAASHSQLPGA"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
