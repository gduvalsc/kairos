class UserObject(dict):
    def __init__(s):
        if "DBORAWEB" not in kairos: kairos['DBORAWEB']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSEWEBNUM",
            "collection": "DBORAWEB",
            "nocache": True,
            "request": "select timestamp, 'number of operations/sec' label, sum(count) value from DBORAWEB where event = '" + kairos["DBORAWEB"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
