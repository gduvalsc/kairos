class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALIBI$$1",
            "collections": [
                "DBORALIB"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, item as label, invalidations as value from DBORALIB) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)