class UserObject(dict):
    def __init__(s):
        if "DBORAHPHVAS" not in kairos: kairos['DBORAHPHVAS']=''
        object = {
            "type": "query",
            "id": "DBORAHPHVASN",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select h.timestamp timestamp, 'Rows' label, sum(rows_processed_delta * 1.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where plan_hash_value = '" + kairos["DBORAHPHVAS"] + "' and h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
