class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUM1$$1",
            "collections": [
                "DBORAWEV"
            ],
            "userfunctions": [
                "idlewev",
                "pxwev"
            ],
            "request": "select timestamp, 'wait events' label, sum(value) value from (select timestamp, event label, time value from DBORAWEV where not idlewev(event) and not pxwev(event)) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)