class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOWS",
            "collection": "DBORASTA",
            "request": "select x.timestamp, 'redo size / write' label, sum(x.value / y.value) value from DBORASTA x, DBORASTA y where x.statistic = 'redo size' and y.statistic in ('redo writes') and x.timestamp = y.timestamp group by x.timestamp, label order by x.timestamp"
        }
        super(UserObject, s).__init__(**object)
