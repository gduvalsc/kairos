class UserObject(dict):
    def __init__(s):
        if "DBORAWEB" not in kairos: kairos['DBORAWEB']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSEWEBAVG",
            "collection": "DBORAWEB",
            "nocache": True,
            "request": "select timestamp, 'average time (ms)' label, sum(1000.0 * time / count) value from DBORAWEB where event = '" + kairos["DBORAWEB"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
