class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHSQLWC$$2",
            "collections": [
                "ORAHQS",
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Captured SQLs' label, sum(value) value from (select timestamp, 'xxx' label, value value from (select h.timestamp timestamp, sql_id, ccwait_delta / 1000000.0 / m.elapsed value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp)) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)