class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISKBSY$$2",
            "collections": [
                "NMONDISKBUSY"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Max busy' label, max(value) value from (select timestamp, 'xxx' label, value value from NMONDISKBUSY) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)