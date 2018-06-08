class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGAA$$1",
            "collections": [
                "DBORASGAA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, sizefactor as label, estphysicalreads as value from DBORASGAA) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)