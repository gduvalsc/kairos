class UserObject(dict):
    def __init__(s):
        if "DBORAHPHVTX" not in kairos: kairos['DBORAHPHVTX']=''
        object = {
            "type": "query",
            "id": "DBORAHPHVTXE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select timestamp, 'elapsed' label, sum(elapsed_time_delta / 1000000.0 / case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where plan_hash_value = '" + kairos["DBORAHPHVTX"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
