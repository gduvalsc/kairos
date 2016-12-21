class UserObject(dict):
    def __init__(s):
        if "DBORAHPHVTX" not in kairos: kairos['DBORAHPHVTX']=''
        object = {
            "type": "query",
            "id": "DBORAHPHVTXWC",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select timestamp, 'Concurrency' label, sum(ccwait_delta / 1000000.0 / case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where plan_hash_value = '" + kairos["DBORAHPHVTX"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
