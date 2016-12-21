class UserObject(dict):
    def __init__(s):
        if "DBORAHPHVSX" not in kairos: kairos['DBORAHPHVSX']=''
        object = {
            "type": "query",
            "id": "DBORAHPHVSXX",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select timestamp, 'Executions' label, sum(executions_delta * 1.0 / case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where plan_hash_value = '" + kairos["DBORAHPHVSX"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
