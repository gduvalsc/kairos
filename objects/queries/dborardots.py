class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOTS",
            "collection": "DBORASTA",
            "request": "select x.timestamp, 'redo write time' label, sum(10.0 * x.value / y.value) value from DBORASTA x, DBORASTA y where x.statistic = 'redo write time' and y.statistic = 'redo writes' and x.timestamp = y.timestamp group by x.timestamp, label order by x.timestamp"
        }
        super(UserObject, s).__init__(**object)
