class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKBSY$$1",
            "collections": [
                "NMONDISKBUSY"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, avg(value) value from (select timestamp, id label, value value from NMONDISKBUSY) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)