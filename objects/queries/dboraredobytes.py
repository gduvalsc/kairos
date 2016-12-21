class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAREDOBYTES",
            "collection": "DBORASTA",
            "request": "select timestamp, statistic label, sum(value) value from DBORASTA where statistic = 'redo size' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
