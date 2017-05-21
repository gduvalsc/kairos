class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVCON$$1",
            "collections": [
                "DBORASVW"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, service label, conwaitt value from DBORASVW) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)