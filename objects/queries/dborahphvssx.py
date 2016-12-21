class UserObject(dict):
    def __init__(s):
        if "DBORAHPHVSS" not in kairos: kairos['DBORAHPHVSS']=''
        object = {
            "type": "query",
            "id": "DBORAHPHVSSX",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select h.timestamp timestamp, 'Executions' label, sum(executions_delta * 1.0 / m.elapsed) value from ORAHQS h, DBORAMISC m where plan_hash_value = '" + kairos["DBORAHPHVSS"] + "' and h.timestamp = m.timestamp group by h.timestamp, label order by h.timestamp"
        }
        super(UserObject, s).__init__(**object)
