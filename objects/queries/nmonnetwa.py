class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONNETWA",
            "collection": "NMONNET",
            "filterable": True,
            "request": "select timestamp, id label, sum(value / 1024.0) value from NMONNET where id like '%write%' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
