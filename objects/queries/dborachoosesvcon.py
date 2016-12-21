class UserObject(dict):
    def __init__(s):
        if "DBORASV" not in kairos: kairos['DBORASV']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSESVCON",
            "collection": "DBORASVW",
            "nocache": True,
            "request": "select timestamp, 'Concurrency wait time' label, sum(conwaitt) value from DBORASVW where service = '" + kairos["DBORASV"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
