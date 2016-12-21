class UserObject(dict):
    def __init__(s):
        if "DBORAHSQLAS" not in kairos: kairos['DBORAHSQLAS']=''
        object = {
            "type": "query",
            "id": "DBORAHSQLASN",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select h.timestamp timestamp, 'Rows' label, sum(rows_processed_delta * 1.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where sql_id = '" + kairos["DBORAHSQLAS"] + "' and h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
