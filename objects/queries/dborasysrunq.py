class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASYSRUNQ",
            "collection": "DBORAOSS",
            "request": "select o.timestamp timestamp, statistic label, sum(value / 100.0 / avgelapsed) value from DBORAOSS o, DBORAMISC m where statistic in ('OS_CPU_WAIT_TIME') and o.timestamp = m.timestamp group by o.timestamp, label order by o.timestamp"
        }
        super(UserObject, s).__init__(**object)
