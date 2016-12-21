class UserObject(dict):
    def __init__(s):
        if "DBORAHFMSTX" not in kairos: kairos['DBORAHFMSTX']=''
        object = {
            "type": "query",
            "id": "DBORAHFMSTXWI",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select timestamp, 'User I/O' label, sum(iowait_delta / 1000000.0 / case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where force_matching_signature = '" + kairos["DBORAHFMSTX"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
