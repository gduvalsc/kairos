class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVADM",
            "collection": "DBORASVW",
            "filterable": True,
            "request": "select timestamp, service label, sum(admwaitt) value from DBORASVW group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
