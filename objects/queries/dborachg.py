class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHG",
            "collection": "DBORASTA",
            "request": "select timestamp, statistic label,  sum(value) value from DBORASTA where statistic in ('consistent changes','db block changes','physical writes','physical writes direct','physical writes direct (lob)','lob writes','physical writes from cache','physical write IO requests') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
