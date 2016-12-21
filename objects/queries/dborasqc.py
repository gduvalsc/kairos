class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQC",
            "collection": "DBORASQC",
            "filterable": True,
            "request": "select timestamp, sqlid label, sum(cpu) value from DBORASQC group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
