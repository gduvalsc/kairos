class UserObject(dict):
    def __init__(s):
        if "DBORAHPHVAX" not in kairos: kairos['DBORAHPHVAX']=''
        object = {
            "type": "query",
            "id": "DBORAHPHVAXN",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select timestamp, 'Rows' label, sum(rows_processed_delta * 1.0 / case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where plan_hash_value = '" + kairos["DBORAHPHVAX"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
