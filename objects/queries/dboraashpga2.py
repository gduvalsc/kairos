class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHPGA2",
            "collection": "ORAHAS",
            "filterable": True,
            "request": "select timestamp, sql_id label, sum(pga_allocated) value from ORAHAS where sql_id != '' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
