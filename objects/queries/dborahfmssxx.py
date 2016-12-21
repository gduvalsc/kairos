class UserObject(dict):
    def __init__(s):
        if "DBORAHFMSSX" not in kairos: kairos['DBORAHFMSSX']=''
        object = {
            "type": "query",
            "id": "DBORAHFMSSXX",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select timestamp, 'Executions' label, sum(executions_delta * 1.0 / case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where force_matching_signature = '" + kairos["DBORAHFMSSX"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
