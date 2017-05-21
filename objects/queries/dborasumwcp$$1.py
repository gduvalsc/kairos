class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUMWCP$$1",
            "collections": [
                "DBORAWEC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, eclass label, time value from DBORAWEC where eclass not in ('DB CPU')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)