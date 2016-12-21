class UserObject(dict):
    def __init__(s):
        if "DBORASV" not in kairos: kairos['DBORASV']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSESVADM",
            "collection": "DBORASVW",
            "nocache": True,
            "request": "select timestamp, 'Administrative wait time' label, sum(admwaitt) value from DBORASVW where service = '" + kairos["DBORASV"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
