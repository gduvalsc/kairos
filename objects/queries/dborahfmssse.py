class UserObject(dict):
    def __init__(s):
        if "DBORAHFMSSS" not in kairos: kairos['DBORAHFMSSS']=''
        object = {
            "type": "query",
            "id": "DBORAHFMSSSE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select h.timestamp timestamp, 'elapsed' label, sum(elapsed_time_delta / 1000000.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where force_matching_signature = '" + kairos["DBORAHFMSSS"] + "' and h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
