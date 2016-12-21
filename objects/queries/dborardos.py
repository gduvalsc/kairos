class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARDOS",
            "collection": "DBORASTA",
            "request": "select timestamp, statistic label, sum(value / 1024.0) value from DBORASTA where statistic = 'redo size' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
