class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACPU",
            "collection": "DBORASTA",
            "request": "select timestamp, statistic label,  sum(cast(value as real) / 100.0) value from DBORASTA where statistic in ('CPU used by this session', 'recursive cpu usage', 'parse time cpu') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
