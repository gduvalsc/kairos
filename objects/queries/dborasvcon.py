class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVCON",
            "collection": "DBORASVW",
            "filterable": True,
            "request": "select timestamp, service label, sum(conwaitt) value from DBORASVW group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
