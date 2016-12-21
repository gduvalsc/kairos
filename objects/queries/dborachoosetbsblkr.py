class UserObject(dict):
    def __init__(s):
        if "DBORATBS" not in kairos: kairos['DBORATBS']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSETBSBLKR",
            "collection": "DBORATBS",
            "nocache": True,
            "request": "select timestamp, 'database blocks per read' label, sum(blocksperread) value from DBORATBS where tablespace = '" + kairos["DBORATBS"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
