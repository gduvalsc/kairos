class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAWEB$$1",
            "collections": [
                "DBORAWEB"
            ],
            "userfunctions": [
                "idlewev",
                "pxwev"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, event label, time value from DBORAWEB where not idlewev(event) and not pxwev(event)) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)