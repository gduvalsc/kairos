class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "TTDBTABLESTATS",
            "collection": "TTSTATS",
            "filterable": True,
            "request": "select timestamp, statistic label, sum(value) value from TTSTATS where statistic like 'db.table.%' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
