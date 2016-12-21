class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONIOADAPTTF",
            "collection": "NMONIOADAPT",
            "filterable": True,
            "request": "select timestamp, id label, sum(value) value from NMONIOADAPT where id like '%xfer%' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
