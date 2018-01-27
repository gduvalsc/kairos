class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOT$$1",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'redo write time' as label, value as value from (select x.timestamp as timestamp, 10.0 * x.value / y. value as value from DBORASTA x, DBORASTA y where x.statistic='redo write time' and y.statistic='redo writes' and x.timestamp = y.timestamp) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)