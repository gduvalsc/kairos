class UserObject(dict):
    def __init__(s):
        if "DBORAHSQLSX" not in kairos: kairos['DBORAHSQLSX']=''
        object = {
            "type": "query",
            "id": "DBORAHSQLSXR",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select timestamp, 'Reads' label, sum(disk_reads_delta * 1.0 / case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where sql_id = '" + kairos["DBORAHSQLSX"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
