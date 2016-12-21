class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAIOAV",
            "collection": "DBORASTA",
            "request": "select timestamp, statistic label,  sum(value) value from DBORASTA where statistic in ('physical read total bytes','physical write total bytes','redo size') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
