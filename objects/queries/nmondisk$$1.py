class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONDISK$$1",
            "collections": [
                "NMONDISKREAD"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Read MB/s' label, sum(value) value from (select timestamp, 'xxx' label, value / 1024.0 value from NMONDISKREAD where id = '%(NMONDISK)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)