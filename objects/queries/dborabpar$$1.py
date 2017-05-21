class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORABPAR$$1",
            "collections": [
                "DBORABPA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, avg(value) value from (select timestamp, sizefactor label, estphysreadsfactor value from DBORABPA where bufpool='R') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)