class UserObject(dict):
    def __init__(s):
        if "DBORASV" not in kairos: kairos['DBORASV']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSESVW",
            "collection": "DBORASRV",
            "nocache": True,
            "request": "select timestamp, 'DB Wait time' label, sum(dbtime - cpu) value from DBORASRV where service = '" + kairos["DBORASV"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
