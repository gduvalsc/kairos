class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVPR$$1",
            "collections": [
                "DBORASRV"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, service label, 1024.0 * reads value from DBORASRV) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)