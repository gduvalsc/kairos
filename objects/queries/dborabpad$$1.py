null=None
true=True
false=False

class UserObject(dict):
    def __init__(self):
        object = {
            "type": "query",
            "id": "DBORABPAD$$1",
            "collections": [
                "DBORABPA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, sizefactor as label, estphysreadsfactor as value from DBORABPA where bufpool='D') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, self).__init__(**object)
