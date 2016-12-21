class UserObject(dict):
    def __init__(s):
        if "DBORAFIL" not in kairos: kairos['DBORAFIL']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSEFILAVG",
            "collection": "DBORAFIL",
            "nocache": True,
            "request": "select timestamp, 'average time (ms)' label, sum(readtime) value from DBORAFIL where file = '" + kairos["DBORAFIL"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
