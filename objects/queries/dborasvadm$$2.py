class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVADM$$2",
            "collections": [
                "DBORAWEC"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'wait events' label, sum(value) value from (select timestamp, 'xxx' label, time value from DBORAWEC where eclass != 'DB CPU') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)