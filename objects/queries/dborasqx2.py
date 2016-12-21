class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQX2",
            "collection": "DBORASTA",
            "request": "select timestamp, statistic label, sum(value) value from DBORASTA where statistic = 'execute count' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
