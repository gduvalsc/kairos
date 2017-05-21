class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALIBI$$2",
            "collections": [
                "DBORALIB"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Invalidations' label, sum(value) value from (select timestamp, 'xxx' label, invalidations value from DBORALIB) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)