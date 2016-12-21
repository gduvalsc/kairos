class UserObject(dict):
    def __init__(s):
        if "NMONDISK" not in kairos: kairos['NMONDISK']=''
        object = {
            "type": "query",
            "id": "NMONDISK1",
            "collection": "NMONDISKREAD",
            "nocache": True,
            "request": "select timestamp, 'Read MB/s' label, sum(value / 1024.0) value from NMONDISKREAD where id = '" + kairos["NMONDISK"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
