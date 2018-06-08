class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVNET$$1",
            "collections": [
                "DBORASVW"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, service as label, netwaitt as value from DBORASVW) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)