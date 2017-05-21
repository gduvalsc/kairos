class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUM$$1",
            "collections": [
                "DBORAWEC"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'wait events' label, sum(value) value from (select timestamp, eclass label, time value from DBORAWEC where eclass not in ('DB CPU')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)