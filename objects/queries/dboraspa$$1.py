class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASPA$$1",
            "collections": [
                "DBORASPA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, sizefactor as label, estloadtimefctr as value from DBORASPA) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)