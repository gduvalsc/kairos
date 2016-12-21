class UserObject(dict):
    def __init__(s):
        if "DBORAHSQLTX" not in kairos: kairos['DBORAHSQLTX']=''
        object = {
            "type": "query",
            "id": "DBORAHSQLTXWA",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select timestamp timestamp, 'Application' label, sum(apwait_delta / 1000000.0 / case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where sql_id = '" + kairos["DBORAHSQLTX"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
