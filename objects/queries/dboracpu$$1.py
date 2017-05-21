class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACPU$$1",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, statistic label, cast(value as real) / 100.0 value from DBORASTA where statistic in ('CPU used by this session', 'recursive cpu usage', 'parse time cpu')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)