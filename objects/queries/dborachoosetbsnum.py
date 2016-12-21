class UserObject(dict):
    def __init__(s):
        if "DBORATBS" not in kairos: kairos['DBORATBS']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSETBSNUM",
            "collection": "DBORATBS",
            "nocache": True,
            "request": "select timestamp, 'number of reads per sec' label, sum(reads) value from DBORATBS where tablespace = '" + kairos["DBORATBS"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
