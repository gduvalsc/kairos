class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQE",
            "collection": "DBORASQE",
            "filterable": True,
            "request": "select timestamp, sqlid label, sum(elapsed) value from DBORASQE group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
