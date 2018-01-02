class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSV$$1",
            "collections": [
                "ORAHQS"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label , sum(value) as value from (select timestamp, force_matching_signature as label, version_count as value from ORAHQS) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)