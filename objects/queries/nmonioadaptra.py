class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONIOADAPTRA",
            "collection": "NMONIOADAPT",
            "filterable": True,
            "request": "select timestamp, id label, sum(value / 1024.0) value from NMONIOADAPT where id like '%read%' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
