class UserObject(dict):
    def __init__(s):
        if "DBORAHPHVTS" not in kairos: kairos['DBORAHPHVTS']=''
        object = {
            "type": "query",
            "id": "DBORAHPHVTSE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select h.timestamp timestamp, 'elapsed' label, sum(elapsed_time_delta / 1000000.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where plan_hash_value = '" + kairos["DBORAHPHVTS"] + "' and h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
