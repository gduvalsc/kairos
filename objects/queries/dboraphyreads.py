class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPHYREADS",
            "collection": "DBORASTA",
            "request": "select timestamp, statistic label, sum(value) value from DBORASTA where statistic = 'physical reads' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
