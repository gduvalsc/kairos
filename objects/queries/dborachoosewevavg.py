class UserObject(dict):
    def __init__(s):
        if "DBORAWEV" not in kairos: kairos['DBORAWEV']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSEWEVAVG",
            "collection": "DBORAWEV",
            "nocache": True,
            "request": "select timestamp, 'average time (ms)' label, sum(1000.0 * time / count) value from DBORAWEV where event = '" + kairos["DBORAWEV"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
