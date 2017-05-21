class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHSQLTS$$4",
            "collections": [
                "ORAHQS",
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Cluster' label, sum(value) value from (select timestamp, 'xxx' label, value value from (select h.timestamp timestamp, clwait_delta / 1000000.0 / m.elapsed value from ORAHQS h, DBORAMISC m where sql_id='%(DBORAHSQLTS)s' and h.timestamp=m.timestamp)) group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)