class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALOGREADS",
            "collection": "DBORASTA",
            "request": "select timestamp, statistic label, sum(value) value from DBORASTA where statistic = 'session logical reads' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
