class UserObject(dict):
    def __init__(s):
        if "DBORAHFMSTS" not in kairos: kairos['DBORAHFMSTS']=''
        object = {
            "type": "query",
            "id": "DBORAHFMSTSC",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select h.timestamp timestamp, 'cpu' label, sum(cpu_time_delta / 1000000.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where force_matching_signature = '" + kairos["DBORAHFMSTS"] + "' and h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
