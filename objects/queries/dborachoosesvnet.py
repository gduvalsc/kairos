class UserObject(dict):
    def __init__(s):
        if "DBORASV" not in kairos: kairos['DBORASV']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSESVNET",
            "collection": "DBORASVW",
            "nocache": True,
            "request": "select timestamp, 'Network wait time' label, sum(netwaitt) value from DBORASVW where service = '" + kairos["DBORASV"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
