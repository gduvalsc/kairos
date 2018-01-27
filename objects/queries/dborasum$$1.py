class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUM$$1",
            "collections": [
                "DBORAWEC"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'wait events' as label, sum(value) as value from (select timestamp, eclass as label, time as value from DBORAWEC where eclass not in ('DB CPU')) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)