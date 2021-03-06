null=None
true=True
false=False

class UserObject(dict):
    def __init__(self):
        object = {
            "type": "query",
            "id": "SNAPPERWEVSES$$1",
            "collections": [
                "SNAPPER"
            ],
            "userfunctions": [
                "snappercoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, sid||' - '||program as label, pthread / 100 /snappercoeff as value from SNAPPER, (select snappercoeff() as snappercoeff) as foo where event = '%(SNAPPERWEVSES)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, self).__init__(**object)
