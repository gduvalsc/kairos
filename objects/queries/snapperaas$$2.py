class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SNAPPERAAS$$2",
            "collections": [
                "SNAPPER"
            ],
            "userfunctions": [
                "snappercoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'waiting'::text as label, pthread /100 /snappercoeff as value from SNAPPER, (select snappercoeff() as snappercoeff) as foo where event != 'ON CPU') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)