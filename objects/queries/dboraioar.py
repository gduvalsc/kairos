class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAIOAR",
            "collection": "DBORASTA",
            "request": "select timestamp, statistic label,  sum(value) value from DBORASTA where statistic in ('physical read total IO requests','physical write total IO requests') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
