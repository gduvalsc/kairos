class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACOM",
            "collection": "DBORASTA",
            "request": "select timestamp, statistic label, sum(value) value from DBORASTA where statistic in ('user commits', 'user rollbacks', 'transaction rollbacks') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
