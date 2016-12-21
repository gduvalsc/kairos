class UserObject(dict):
    def __init__(s):
        if "NMONDISK" not in kairos: kairos['NMONDISK']=''
        object = {
            "type": "query",
            "id": "NMONDISK3",
            "collection": "NMONDISKBUSY",
            "nocache": True,
            "request": "select timestamp, 'Busy rate %' label, avg(value) value from NMONDISKBUSY where id = '" + kairos["NMONDISK"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
