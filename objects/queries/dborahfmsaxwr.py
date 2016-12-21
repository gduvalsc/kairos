class UserObject(dict):
    def __init__(s):
        if "DBORAHFMSAX" not in kairos: kairos['DBORAHFMSAX']=''
        object = {
            "type": "query",
            "id": "DBORAHFMSAXWR",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select timestamp, 'Cluster' label, sum(clwait_delta / 1000000.0 / case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where force_matching_signature = '" + kairos["DBORAHFMSAX"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
