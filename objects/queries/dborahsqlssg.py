class UserObject(dict):
    def __init__(s):
        if "DBORAHSQLSS" not in kairos: kairos['DBORAHSQLSS']=''
        object = {
            "type": "query",
            "id": "DBORAHSQLSSG",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select h.timestamp timestamp, 'Gets' label, sum(buffer_gets_delta * 1.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where sql_id = '" + kairos["DBORAHSQLSS"] + "' and h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
