class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPGAA$$1",
            "collections": [
                "DBORAPMA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, sizefactor as label, estextrabytesrw as value from DBORAPMA) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)