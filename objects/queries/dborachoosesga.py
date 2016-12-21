class UserObject(dict):
    def __init__(s):
        if "DBORASGA" not in kairos: kairos['DBORASGA']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSESGA",
            "collection": "DBORASGA",
            "nocache": True,
            "request": "select timestamp, pool||' '||name label, sum(size) value from DBORASGA where pool||' '||name = '" + kairos["DBORASGA"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
