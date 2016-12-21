class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORADBTIME",
            "collection": "DBORATMS",
            "request": "select timestamp, statistic label, sum(time) value from DBORATMS where statistic = 'DB time' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
