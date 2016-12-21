class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHPGA",
            "collection": "ORAHAS",
            "filterable": True,
            "request": "select timestamp, session_id||' - '||program  label, sum(pga_allocated) value from ORAHAS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
