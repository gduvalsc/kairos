class UserObject(dict):
    def __init__(s):
        if "TTSTA" not in kairos: kairos['TTSTA']=''
        object = {
            "type": "query",
            "id": "TTSTA",
            "collection": "TTSTATS",
            "nocache": True,
            "request": "select timestamp, statistic label, sum(value) value from TTSTATS where statistic = '" + kairos["TTSTA"] + "'  group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
