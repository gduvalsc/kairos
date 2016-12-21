class UserObject(dict):
    def __init__(s):
        if "DBORATBS" not in kairos: kairos['DBORATBS']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSETBSAVG",
            "collection": "DBORATBS",
            "nocache": True,
            "request": "select timestamp, 'average time (ms)' label, sum(readtime) value from DBORATBS where tablespace = '" + kairos["DBORATBS"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
