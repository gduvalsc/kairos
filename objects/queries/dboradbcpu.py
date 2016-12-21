class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORADBCPU",
            "collection": "DBORATMS",
            "request": "select timestamp, 'DB CPU' label, sum(time) value from DBORATMS where statistic = 'DB CPU' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
