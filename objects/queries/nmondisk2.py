class UserObject(dict):
    def __init__(s):
        if "NMONDISK" not in kairos: kairos['NMONDISK']=''
        object = {
            "type": "query",
            "id": "NMONDISK2",
            "collection": "NMONDISKWRITE",
            "nocache": True,
            "request": "select timestamp, 'Write MB/s' label, sum(value / 1024.0) value from NMONDISKWRITE where id = '" + kairos["NMONDISK"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
