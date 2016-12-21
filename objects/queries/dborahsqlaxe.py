class UserObject(dict):
    def __init__(s):
        if "DBORAHSQLAX" not in kairos: kairos['DBORAHSQLAX']=''
        object = {
            "type": "query",
            "id": "DBORAHSQLAXE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select timestamp, 'elapsed' label, sum(elapsed_time_delta / 1000000.0 / case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where sql_id = '" + kairos["DBORAHSQLAX"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
