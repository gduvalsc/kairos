class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQW",
            "collection": "DBORASQW",
            "filterable": True,
            "request": "select timestamp, sqlid label, sum(clusterwait) value from DBORASQW group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
