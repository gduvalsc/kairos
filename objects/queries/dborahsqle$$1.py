class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHSQLE$$1",
            "collections": [
                "ORAHQS",
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, sql_id label, value value from (select h.timestamp timestamp, sql_id, elapsed_time_delta / 1000000.0 / m.elapsed value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp)) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)