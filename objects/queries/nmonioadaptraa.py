class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONIOADAPTRAA",
            "collection": "NMONIOADAPT",
            "request": "select timestamp, 'All adapters (read)' label, sum(value / 1024.0) value from NMONIOADAPT where id like '%read%' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
