class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGDPW1",
            "collection": "DBORASTA",
            "request": "select timestamp, statistic label, sum(value) value from DBORASTA where statistic in ('physical writes', 'physical writes direct') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
