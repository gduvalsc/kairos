class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASYS$$2",
            "collections": [
                "DBORAOSS"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, statistic label, value value from DBORAOSS where statistic='NUM_CPUS') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)