class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONSYS$$1",
            "collections": [
                "NMONPROC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, id label, value value from NMONPROC) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)