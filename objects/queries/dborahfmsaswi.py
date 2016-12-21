class UserObject(dict):
    def __init__(s):
        if "DBORAHFMSAS" not in kairos: kairos['DBORAHFMSAS']=''
        object = {
            "type": "query",
            "id": "DBORAHFMSASWI",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select h.timestamp timestamp, 'User I/O' label, sum(iowait_delta / 1000000.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where force_matching_signature = '" + kairos["DBORAHFMSAS"] + "' and h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
