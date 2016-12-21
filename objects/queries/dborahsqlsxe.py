class UserObject(dict):
    def __init__(s):
        if "DBORAHSQLSX" not in kairos: kairos['DBORAHSQLSX']=''
        object = {
            "type": "query",
            "id": "DBORAHSQLSXE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select timestamp, 'elapsed' label, sum(elapsed_time_delta / 1000000.0 / case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where sql_id = '" + kairos["DBORAHSQLSX"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
