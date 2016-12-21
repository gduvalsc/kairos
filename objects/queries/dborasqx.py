class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQX",
            "collection": "DBORASQX",
            "filterable": True,
            "request": "select timestamp, sqlid label, sum(execs) value from DBORASQX group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
