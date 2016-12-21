class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASYSLOAD",
            "collection": "DBORAOSS",
            "request": "select timestamp, statistic label, sum(value) value from DBORAOSS where statistic in ('LOAD') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
