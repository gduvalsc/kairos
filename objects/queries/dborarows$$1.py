class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAROWS$$1",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [
                "meet"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, statistic as label, value as value from DBORASTA where meet(statistic, '(table fetch|table scan rows)')) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)