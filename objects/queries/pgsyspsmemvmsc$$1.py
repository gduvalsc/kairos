null=None
true=True
false=False

class UserObject(dict):
    def __init__(self):
        object = {
            "type": "query",
            "id": "PGSYSPSMEMVMSC$$1",
            "collections": [
                "vpsutil_processes"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, pname as label, vms::real as value from vpsutil_processes) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, self).__init__(**object)
