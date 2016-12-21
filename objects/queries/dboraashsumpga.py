class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSUMPGA",
            "collection": "ORAHAS",
            "request": "select timestamp, 'PGA allocated' label, sum(pga_allocated) value from ORAHAS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
