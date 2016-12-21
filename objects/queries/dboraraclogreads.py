class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACLOGREADS",
            "collection": "DBORARACSTA",
            "request": "select timestamp, statistic label, sum(value) value from DBORARACSTA where statistic = 'session logical reads' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
