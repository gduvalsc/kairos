class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQP",
            "collection": "DBORASQP",
            "filterable": True,
            "request": "select timestamp, sqlid label, sum(parses) value from DBORASQP group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
