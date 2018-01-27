class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORABPAK$$1",
            "collections": [
                "DBORABPA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, sizefactor as label, estphysreadsfactor as value from DBORABPA where bufpool='K') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)