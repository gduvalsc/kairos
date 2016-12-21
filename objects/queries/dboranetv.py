class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORANETV",
            "collection": "DBORASTA",
            "userfunctions": ['match'],
            "request": "select timestamp, statistic label, sum(value / 1024.0) value from DBORASTA where match(statistic, '(bytes)') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
