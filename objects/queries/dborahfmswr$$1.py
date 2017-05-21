class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHFMSWR$$1",
            "collections": [
                "ORAHQS",
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, force_matching_signature label, value value from (select h.timestamp timestamp, force_matching_signature, clwait_delta / 1000000.0 / m.elapsed value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp)) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)