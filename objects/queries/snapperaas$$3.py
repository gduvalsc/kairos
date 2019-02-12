class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SNAPPERAAS$$3",
            "collections": [
                "SNAPPER"
            ],
            "userfunctions": [
                "snappercoeff"
            ],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, 'average active sessions'::text as label, aas/snappercoeff as value from SNAPPER, (select snappercoeff() as snappercoeff) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)