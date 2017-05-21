class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOW$$1",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'redo size / write' label, sum(value) value from (select timestamp, 'xxx' label, value value from (select x.timestamp timestamp, x.value / y.value value from DBORASTA x, DBORASTA y where x.statistic = 'redo size' and y.statistic = 'redo writes' and x.timestamp = y.timestamp)) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)