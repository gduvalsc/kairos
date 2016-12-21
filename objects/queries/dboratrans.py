class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORATRANS",
            "collection": "DBORASTA",
            "request": "select timestamp, 'user transactions' label, sum(value) value from DBORASTA where statistic in ('user rollbacks', 'user commits') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
